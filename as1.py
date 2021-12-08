import time
import random
# import streamlit as st

# st.title("Avtaar")
name=input("Enter your Name:")
lower="abcefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
all=lower+upper+number
length=6
unique_id="".join(random.sample(all,length))
print(name)
print(unique_id)
a=time.localtime()
c=time.asctime(a)
print(c)