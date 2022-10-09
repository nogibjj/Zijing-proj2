#!/usr/bin/env python
chmod +x query.py
./query.py describe
./query.py query-most-n --n 10
streamlit run app.py --server.enableCORS=false