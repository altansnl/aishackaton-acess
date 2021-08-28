# Importing stock libraries
import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, RandomSampler, SequentialSampler
from transformers import TFAutoModel

# Importing the T5 modules from huggingface/transformers
from transformers import T5Tokenizer, T5ForConditionalGeneration
from datasets import load_dataset

"""
dataset = load_dataset('multi_news', split='test')
original_text = dataset[10]['document']
"""

original_text = "To be able to perform face recognition, the projected used state of the art neural networks"

def summarizeWithT5(original_text, model, tokenizer, num_beams=1, temperature=1.0, top_k=1, top_p=1.0):
    text = "summarize:" + original_text
    input_ids = tokenizer.encode(text, return_tensors='pt', max_length=50, truncation=True)
    summary_ids = model.generate(input_ids, max_length=50, min_length=20, top_k=top_k, top_p=top_p, num_beams=num_beams, temperature=temperature, early_stopping=True)
    t5_summary = tokenizer.decode(summary_ids[0])
    return t5_summary

PATH = 'Chris 9_54'
model_imported = T5ForConditionalGeneration.from_pretrained(PATH)
tokenizer = T5Tokenizer.from_pretrained("t5-small")

print(summarizeWithT5(original_text, model_imported, tokenizer))