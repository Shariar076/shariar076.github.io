---
title: "ASR System for Patient Symptoms"
excerpt: "Healthcare AI · Speech AI<br/><img src='/images/medai_asr.png' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** Healthcare AI · Speech AI

ASR system for understanding medical symptoms spoken by patients in Bengali. Trained **DeepSpeech** from scratch on audio collected via a consented data collection portal, then finetuned for noisy environments using 13 domain augmentations. Switched to a **Whisper** (tiny) model finetuned on the BanglaASR corpus (Bangla Mozilla Common Voice), achieving a WER of only 8%—enabled by the limited vocabulary of symptom terms.

[Slides](https://docs.google.com/presentation/d/1ac6pA46bzN0P9236wpypY2uipZwa00evz3bRxdL9tU0/edit?usp=sharing) · [Live demo on Hugging Face](https://huggingface.co/spaces/MedAiHealth/asr-test)
