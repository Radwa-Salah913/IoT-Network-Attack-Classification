import pickle
import streamlit as st
import pandas as pd

import os
file_path = 'C:/Users/dell/OneDrive/Desktop/ML/Preprocessing/attack model.sav'
if os.path.exists(file_path):
    model = pickle.load(open(file_path, 'rb'))
else:
    st.error(f"File not found: {file_path}")

st.title('Detect Attack Type')

columns_name=['bwd_pkts_per_sec', 'flow_iat.std', 'active.tot',
       'flow_pkts_payload.max', 'flow_pkts_payload.min', 'flow_iat.tot',
       'bwd_header_size_max', 'down_up_ratio', 'fwd_subflow_pkts',
       'fwd_header_size_max', 'bwd_pkts_payload.tot', 'active.min',
       'bwd_iat.min', 'flow_pkts_payload.avg', 'id.resp_p', 'bwd_iat.max',
       'fwd_last_window_size', 'fwd_pkts_payload.avg', 'bwd_iat.tot',
       'flow_iat.min', 'fwd_psh_flag_count', 'fwd_subflow_bytes',
       'fwd_pkts_payload.min', 'fwd_pkts_payload.tot', 'fwd_iat.min',
       'id.orig_p', 'flow_rst_flag_count'] 

dic={}
for i in columns_name:
    temp = st.text_input(i)
    try:
        dic[i] = [float(temp)] if temp else [0]  # Handle empty input with default value
    except ValueError:
        st.error(f"Invalid input for {i}. Please enter a numeric value.")
        dic[i] = [0]  # You can use 0 or any other default value

proto=st.selectbox('proto',['icmp', 'tcp', 'udp'])
service=st.selectbox('service',['-', 'dhcp','dns', 'http', 'irc', 'mqtt', 'ntp', 'radius', 'ssh', 'ssl'])

if(proto=='icmp') :
    dic['icmp']=[1]
    dic['tcp']=[0]
    dic['udp']=[0]
elif proto=='tcp':
    dic['icmp']=[0]
    dic['tcp']=[1]
    dic['udp']=[0]
else:
    dic['icmp']=[0]
    dic['tcp']=[0]
    dic['udp']=[1]


if service=='-':
    dic['-']=[1]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='dhcp'):
    dic['-']=[0]
    dic['dhcp']=[1]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='dns'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[1]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='http'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[1]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='irc'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[1]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='mqtt'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[1]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='ntp'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[1]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='radius'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[1]
    dic['ssh']=[0]
    dic['ssl']=[0]
elif(service=='ssh'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[1]
    dic['ssl']=[0]
elif(service=='ssl'):
    dic['-']=[0]
    dic['dhcp']=[0]
    dic['dns']=[0]
    dic['http']=[0]
    dic['irc']=[0]
    dic['mqtt']=[0]
    dic['ntp']=[0]
    dic['radius']=[0]
    dic['ssh']=[0]
    dic['ssl']=[1]


df=pd.DataFrame(dic,index=[0])

#st.sidebar.header('Feature selection')
con=st.button('Confirm')

if con:
    result=model.predict(df)
    if result==2:
        st.write('DOS_SYN_Hping')
    elif result==10: 
        st.write('Thing_Speak') 
    elif result==0: 
        st.write('ARP_poisioning')  
    elif result==3: 
        st.write('MQTT_Publish')    
    elif result==8: 
        st.write('NMAP_UDP_SCAN ')
    elif result==9: 
        st.write('NMAP_XMAS_TREE_SCAN ')
    elif result==6: 
        st.write('NMAP_OS_DETECTION')
    elif result==7: 
        st.write('NMAP_TCP_scan ')  
    elif result==1: 
        st.write('DDOS_Slowloris ')    
    elif result==11: 
        st.write('Wipro_bulb  ')
    elif result==4: 
        st.write('Metasploit_Brute_Force_SSH ')
    elif result==5: 
        st.write('NMAP_FIN_SCAN ')