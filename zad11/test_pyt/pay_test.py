from unittest.mock import MagicMock
from zad11.database import Contact

def test_create_contact(client):

    new_concatct={first_name:"Krystian", last_name:"Nowak", date_of_birth:"1977-05-06"}
    response= client.post("/contact", jeson=new_concatct)
    assert response.status_code==201
    data= response.json()
    assert data[first_name]=="Krystian"
    assert data[last_name]== "Nowak"
    assert data[date_of_birth]=="1977-05-06"