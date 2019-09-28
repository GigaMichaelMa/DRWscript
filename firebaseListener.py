# from google.cloud import firestore
# from google.oauth2 import service_account


# credentials = service_account.Credentials.from_service_account_file(
#     '/home/loli/pyHac/cred.json')
# # Add a new document
# db = firestore.Client(Cred)
# doc_ref = db.collection(u'users').document(u'alovelace')

# # Then query for documents
# users_ref = db.collection(u'users')

# for doc in users_ref.stream():
#     print(u'{} => {}'.format(doc.id, doc.to_dict()))

import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore

cred = credentials.Certificate("./cred.json")
firebase_admin.initialize_app(cred)

store = firestore.client()
doc_ref = store.collection(u'users').limit(2)

try:
    docs = doc_ref.get()
    for doc in docs:
        print(u'Doc Data:{}'.format(doc.to_dict()))
except google.cloud.exceptions.NotFound:
    print(u'Missing data')
