import requests

def test_valid_id_json():
    response = requests.get('http://127.0.0.1:5000/products?source=json&id=24')
    print(response.text)  # Print the raw response text for debugging
    content = response.json()
    assert 'Jarvis' in content['name'], "Failed: Product not found in JSON source"

if __name__ == "__main__":
    test_valid_id_json()
