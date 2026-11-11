import streamlit as st
from donorview import Blooddonormanager

donor_instance = Blooddonormanager()

tab1,tab2,tab3,tab4= st.tabs(["Add Donor", "View Donor", "Update Details", "Delete Details"])
blood_groups=[ "a+ve", "b+ve", "O+"]

with tab1:
    st.header("Add new Donor....!")

    name = st.text_input("Enter donor name")
    phone = st.text_input("Enter donor phone number")
    blood_group = st.selectbox("Select donor Blood group", ["a+ve", "b+ve","O+"])
    city = st.text_input("Enter donor city")
    last_donation = st.date_input("Enter last donation date")

    if st.button("Submit"):
        donor_instance.post(
            name=name,
            phone=phone,
            blood_group=blood_group,
            city=city,
            last_donation=last_donation
        )
        st.success("Donor added successfully....")

with tab2:
    st.header("View Blood Donor Details....!")

    record = donor_instance.get()

    if record:
        for donor in record:
            st.write(donor)
    else:
        st.warning("No donors")
        
with tab3:
    st.title("update donor details")
    record=donor_instance.get()
    if record:
        donor_ids=[r[0] for r in record]                           #donar_ids=[1,3,5]
        id=st.selectbox("select donor id",donor_ids,key="update_id")
        record=donor_instance.get_object(id=id)
        name=st.text_input("enter your name",value=record[1])
        blood_group=st.selectbox("select your blood group",
                                blood_groups,
                                index=blood_groups.index(record[2]),
                                key="update_group")
        phone=st.text_input("enter your phone number", value=record[3])
        city=st.text_input("enter your city",value=record[4])
        last_donation=st.date_input("last donation date",value=record[5])
        
        if st.button("update"):
            status, message=donor_instance.put(id=id,
                                               name=name,
                                               blood_group=blood_group,
                                               phone=phone,
                                               city=city,
                                               last_donation=last_donation)
            if status:
                st.success(message)
            else:
                st.error(message)
    else:
        st.warning("no donor found ")
                
        
        
        
        