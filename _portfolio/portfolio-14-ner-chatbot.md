---
title: "NER From Chatbot User Messages"
excerpt: "NLP · Banking<br/><img src='/images/ie_er.png' style='max-width:400px;'>"
collection: portfolio
---

**Tags:** NLP · Banking

Extraction of named entities (NE) from banking chatbot messages—beneficiary names, transfer amounts, account types, account numbers, etc. Instead of a single model, we used a recipe of approaches: BERT for beneficiary name extraction, RegEx for transfer amounts and account numbers, and lookup tables for account type extraction. This minimized the training burden for Bengali, a low-resource language.
