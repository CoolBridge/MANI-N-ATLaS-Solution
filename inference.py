import torch
import gc
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import PeftModel

# 1. Clear out any lingering VRAM
torch.cuda.empty_cache()
gc.collect()

ADAPTER_PATH = "/content/drive/MyDrive/mani_project/natlas_mani_qlora_output"
BASE_MODEL_ID = "NCAIR1/N-ATLaS"

print("Loading tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(ADAPTER_PATH, trust_remote_code=True)

# 2. Configure 4-bit quantization to prevent OOM errors
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True
)

print("Loading base model in 4-bit quantization...")
base_model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL_ID,
    quantization_config=quantization_config,
    device_map="auto",
    trust_remote_code=True
)

print("Loading fine-tuned MANI LoRA adapter...")
model = PeftModel.from_pretrained(base_model, ADAPTER_PATH)
model.eval()

# Sample public health test prompt blending CHIRPS, NDVI, and DHS biomarker inputs
test_prompt = (
    "Context: Satellite telemetry indicates a 35% increase in CHIRPS precipitation anomalies and a rising NDVI vector habitat index across LGA North. "
    "DHS biomarker survey logs report an RDT parasitemia prevalence of 28% and low household ITN (insecticide-treated net) usage rates.\n\n"
    "Question: Based on these epidemiological indicators, what immediate targeted resource allocation and intervention should the state health manager prioritize for this zone?\n\n"
    "Answer:"
)

print("\n--- Generating MANI Response ---")
inputs = tokenizer(test_prompt, return_tensors="pt").to("cuda")

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.7,
        do_sample=True,
        top_p=0.9,
        pad_token_id=tokenizer.eos_token_id
    )

decoded_output = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(decoded_output)
