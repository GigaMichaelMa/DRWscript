from google.cloud import firestore
from google.oauth2 import service_account


credentials = service_account.Credentials.from_service_account_file(
    '/path/to/key.json')
# Add a new document
db = firestore.Client()
doc_ref = db.collection(u'users').document(u'alovelace')

# Then query for documents
users_ref = db.collection(u'users')

for doc in users_ref.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
