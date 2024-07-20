"""
ECB cut and paste
"""
import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Step 1: Parsing k=v Strings
def kv_parse(kv_string):
    parsed_dict = {}
    pairs = kv_string.split('&')
    for pair in pairs:
        key, value = pair.split('=')
        parsed_dict[key] = value
    return parsed_dict

# Step 2: Creating a Profile
def profile_for(email):
    # Sanitize the email to prevent metacharacters
    email = email.replace('&', '').replace('=', '')
    profile = {
        'email': email,
        'uid': 10,
        'role': 'user'
    }
    # Encode the profile as a k=v string
    encoded_profile = f"email={profile['email']}&uid={profile['uid']}&role={profile['role']}"
    return encoded_profile

# Step 3: Encrypting and Decrypting Profiles
# Generate a random AES key
aes_key = get_random_bytes(16)

def encrypt_profile(profile, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_profile = pad(profile.encode(), AES.block_size)
    ciphertext = cipher.encrypt(padded_profile)
    return ciphertext

def decrypt_profile(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted.decode()

# Step 4: Crafting the Admin Profile
def create_admin_profile():
    email1 = "foo@bar.com"  # Regular email
    email2 = "foo@bar.admin" + chr(11) * 11  # email to align 'admin' to its own block

    # Encrypt profiles
    encrypted_profile1 = encrypt_profile(profile_for(email1), aes_key)
    encrypted_profile2 = encrypt_profile(profile_for(email2), aes_key)

    # Decrypt to verify

    # Extract blocks
    block_size = AES.block_size
    block1 = encrypted_profile1[:block_size]  # email=foo@bar.
    block2 = encrypted_profile1[block_size:2*block_size]  # com&uid=10&rol
    block5 = encrypted_profile2[2*block_size:3*block_size]  # e=admin\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b\x0b

    # Construct new ciphertext with role=admin
    crafted_ciphertext = block1 + block2 + block5

    # Decrypt the crafted ciphertext
    crafted_profile = decrypt_profile(crafted_ciphertext, aes_key)
    print("Crafted Profile:", crafted_profile)
    return crafted_profile

# Example usage
if __name__ == "__main__":
    kv_string = "foo=bar&baz=qux&zap=zazzle"
    parsed = kv_parse(kv_string)
    print("Parsed KV String:", parsed)

    create_admin_profile()

