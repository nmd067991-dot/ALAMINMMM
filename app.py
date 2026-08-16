import requests, os, psutil, sys, jwt, pickle, json, binascii, time, urllib3, base64, datetime, re, socket, threading, ssl, pytz, aiohttp, random, asyncio
from flask import Flask, request, jsonify
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from cfonts import render

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ============= GLOBALS =============
online_writer = None
whisper_writer = None
spam_room = False
spammer_uid = None
spam_chat_id = None
spam_uid = None
Spy = False
Chat_Leave = False
key = None
iv = None
region = None
BOT_UID = None
loop = None

app = Flask(__name__)

Hr = {
    'User-Agent': "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)",
    'Connection': "Keep-Alive",
    'Accept-Encoding': "gzip",
    'Content-Type': "application/x-www-form-urlencoded",
    'Expect': "100-continue",
    'X-Unity-Version': "2018.4.11f1",
    'X-GA': "v1 1",
    'ReleaseVersion': "OB53"
}

# ============= HELPER FUNCTIONS =============
def get_random_color():
    colors = ["[FF0000]", "[00FF00]", "[0000FF]", "[FFFF00]", "[FF00FF]", "[00FFFF]", "[FFFFFF]", "[FFA500]"]
    return random.choice(colors)

def xMsGFixinG(text):
    """Simple encryption/obfuscation"""
    return str(text)

async def Ua():
    return "Dalvik/2.1.0 (Linux; U; Android 11; ASUS_Z01QD Build/PI)"

async def encrypted_proto(encoded_hex):
    """Encrypt with AES-CBC"""
    key_bytes = b'Yg&tc%DEuh6%Zc^8'
    iv_bytes = b'6oyZDr22E3ychjM%'
    cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)
    padded = pad(encoded_hex, AES.block_size)
    return cipher.encrypt(padded)

async def DecodE_HeX(hex_string):
    """Convert hex to bytes"""
    return bytes.fromhex(str(hex_string))

async def EnC_PacKeT(packet, key, iv):
    """Encrypt packet"""
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv.encode())
    padded = pad(packet.encode(), AES.block_size)
    return cipher.encrypt(padded).hex()

async def DeCode_PackEt(hex_data):
    """Decode packet - mock implementation"""
    try:
        # Simple decode for testing
        return json.dumps({"status": "ok", "data": hex_data[:50]})
    except:
        return json.dumps({"status": "error"})

async def GeTSQDaTa(packet):
    """Get squad data - mock"""
    return ("1234567890", "1234567890", "1234567890")

async def AutH_Chat(chat_type, uid, chat_id, key, iv):
    """Auth chat - mock"""
    return "0" * 50

async def AuthClan(clan_id, compiled_data, key, iv):
    """Auth clan - mock"""
    return "0" * 50

async def OpEnSq(key, iv, region):
    """Open squad - mock"""
    return "0" * 50

async def cHSq(uid, target, key, iv, region):
    """Create squad - mock"""
    return "0" * 50

async def SEnd_InV(uid, target, key, iv, region):
    """Send invite - mock"""
    return "0" * 50

async def ExiT(uid, key, iv):
    """Exit squad - mock"""
    return "0" * 50

async def GenJoinSquadsPacket(team_code, key, iv):
    """Join squad packet - mock"""
    return "0" * 50

async def FS(key, iv):
    """Find squad - mock"""
    return "0" * 50

async def Emote_k(uid, emote_id, key, iv, region):
    """Emote packet - mock"""
    return "0" * 50

async def xSEndMsgsQ(message, chat_id, key, iv):
    """Send squad message - mock"""
    return "0" * 50

async def xSEndMsg(message, chat_type, uid, chat_id, key, iv):
    """Send message - mock"""
    return "0" * 50

async def equie_emote(token, url):
    """Initialize emote - mock"""
    pass

# ============= MAIN FUNCTIONS =============
async def GeNeRaTeAccEss(uid, password):
    """Generate access token"""
    url = "https://100067.connect.garena.com/oauth/guest/token/grant"
    data = {
        "uid": uid,
        "password": password,
        "response_type": "token",
        "client_type": "2",
        "client_secret": "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        "client_id": "100067"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=Hr, data=data) as response:
            if response.status != 200:
                return (None, None)
            data = await response.json()
            return (data.get("open_id"), data.get("access_token"))

async def EncRypTMajoRLoGin(open_id, access_token):
    """Encrypt major login"""
    # Simplified for demonstration
    return b"encrypted_data"

async def MajorLogin(payload):
    """Major login request"""
    url = "https://loginbp.ggblueshark.com/MajorLogin"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTMajoRLoGin(data):
    """Decrypt major login response - mock"""
    class MockResponse:
        url = "https://mock.garena.com"
        region = "US"
        token = "mock_token"
        account_uid = 1234567890
        key = "mockkey1234567890"
        iv = "mockiv1234567890"
        timestamp = 1234567890
    return MockResponse()

async def GetLoginData(base_url, payload, token):
    """Get login data"""
    url = f"{base_url}/GetLoginData"
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    Hr['Authorization'] = f"Bearer {token}"
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, headers=Hr, ssl=ssl_context) as response:
            if response.status == 200:
                return await response.read()
            return None

async def DecRypTLoGinDaTa(data):
    """Decrypt login data - mock"""
    class MockLoginData:
        Online_IP_Port = "127.0.0.1:8080"
        AccountIP_Port = "127.0.0.1:8081"
        AccountName = "BOT_ACCOUNT"
        Clan_ID = None
        Clan_Compiled_Data = None
    return MockLoginData()

async def xAuThSTarTuP(target, token, timestamp, key, iv):
    """Auth startup packet"""
    return "0" * 100

async def cHTypE(chat_type):
    """Get chat type"""
    if not chat_type:
        return 'Squid'
    elif chat_type == 1:
        return 'CLan'
    elif chat_type == 2:
        return 'PrivaTe'
    return 'Squid'

async def SEndMsG(chat_type, message, uid, chat_id, key, iv):
    """Send message"""
    chat_type_str = await cHTypE(chat_type)
    return await xSEndMsg(message, chat_type_str, uid, chat_id, key, iv)

async def SEndPacKeT(writer1, writer2, packet_type, packet):
    """Send packet"""
    if packet_type == 'ChaT' and writer1:
        writer1.write(packet.encode())
        await writer1.drain()
    elif packet_type == 'OnLine' and writer2:
        writer2.write(packet.encode())
        await writer2.drain()

# ============= TCP CONNECTIONS =============
async def TcPOnLine(ip, port, key, iv, auth_token, reconnect_delay=0.5):
    """TCP Online connection"""
    global online_writer, whisper_writer
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            online_writer = writer
            writer.write(bytes.fromhex(auth_token))
            await writer.drain()
            
            while True:
                data = await reader.read(9999)
                if not data:
                    break
                # Process data
                pass
                
            writer.close()
            await writer.wait_closed()
            online_writer = None
        except Exception as e:
            print(f"Online error: {e}")
            online_writer = None
        await asyncio.sleep(reconnect_delay)

async def TcPChaT(ip, port, auth_token, key, iv, login_data, ready_event, region, reconnect_delay=0.5):
    """TCP Chat connection"""
    global whisper_writer, online_writer
    print(f"Chat connection to {ip}:{port}")
    
    while True:
        try:
            reader, writer = await asyncio.open_connection(ip, int(port))
            whisper_writer = writer
            writer.write(bytes.fromhex(auth_token))
            await writer.drain()
            ready_event.set()
            
            while True:
                data = await reader.read(9999)
                if not data:
                    break
                # Process messages
                pass
                
            writer.close()
            await writer.wait_closed()
            whisper_writer = None
        except Exception as e:
            print(f"Chat error: {e}")
            whisper_writer = None
        await asyncio.sleep(reconnect_delay)

# ============= FLASK ROUTES =============
async def perform_emote(team_code: str, uids: list, emote_id: int):
    """Perform emote on targets"""
    global key, iv, region, online_writer, BOT_UID

    if online_writer is None:
        raise Exception("Bot not connected")

    try:
        # Join squad
        join_packet = await GenJoinSquadsPacket(team_code, key, iv)
        await SEndPacKeT(None, online_writer, 'OnLine', join_packet)
        await asyncio.sleep(0.12)

        # Send emotes
        for uid_str in uids:
            uid = int(uid_str)
            emote_packet = await Emote_k(uid, emote_id, key, iv, region)
            await SEndPacKeT(None, online_writer, 'OnLine', emote_packet)

        # Leave squad
        leave_packet = await ExiT(BOT_UID, key, iv)
        await SEndPacKeT(None, online_writer, 'OnLine', leave_packet)
        await asyncio.sleep(0.03)

        return {"status": "success", "message": "Emote done"}
    except Exception as e:
        raise Exception(f"Emote failed: {str(e)}")

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "bot": "FreeFire Emote Bot",
        "endpoints": {
            "/join?tc=CODE&uid1=UID&emote_id=ID": "Trigger emote"
        }
    })

@app.route('/join')
def join_team():
    """API endpoint to trigger emote"""
    global loop
    team_code = request.args.get('tc')
    emote_id_str = request.args.get('emote_id')
    
    # Get all UIDs
    uids = []
    for i in range(1, 7):
        uid = request.args.get(f'uid{i}')
        if uid:
            uids.append(uid)

    if not team_code or not emote_id_str:
        return jsonify({"status": "error", "message": "Missing tc or emote_id"})

    try:
        emote_id = int(emote_id_str)
    except:
        return jsonify({"status": "error", "message": "emote_id must be integer"})

    if not uids:
        return jsonify({"status": "error", "message": "Provide at least one UID"})

    # Run emote in background
    asyncio.run_coroutine_threadsafe(
        perform_emote(team_code, uids, emote_id), 
        loop
    )

    return jsonify({
        "status": "success",
        "team_code": team_code,
        "uids": uids,
        "emote_id": emote_id,
        "message": "Emote triggered"
    })

# ============= FLASK THREAD =============
def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=False, use_reloader=False)

# ============= MAIN BOT =============
async def MaiiiinE():
    global loop, key, iv, region, BOT_UID, online_writer, whisper_writer

    # Bot credentials
    BOT_UID = 16986927594
    Uid, Pw = '6497677576', 'W8Team_W8SOJIB_Uts2cN5cap'

    # Get access token
    open_id, access_token = await GeNeRaTeAccEss(Uid, Pw)
    if not open_id or not access_token:
        print("Error: Invalid account")
        return

    # Major login
    encrypted_login = await EncRypTMajoRLoGin(open_id, access_token)
    login_response = await MajorLogin(encrypted_login)
    if not login_response:
        print("Error: Login failed")
        return

    login_auth = await DecRypTMajoRLoGin(login_response)
    url = login_auth.url
    region = login_auth.region
    token = login_auth.token
    target = login_auth.account_uid
    key = login_auth.key
    iv = login_auth.iv
    timestamp = login_auth.timestamp

    loop = asyncio.get_running_loop()

    # Get login data
    login_data = await GetLoginData(url, encrypted_login, token)
    if not login_data:
        print("Error: Getting ports failed")
        return

    decrypted_data = await DecRypTLoGinDaTa(login_data)
    online_ip, online_port = decrypted_data.Online_IP_Port.split(":")
    chat_ip, chat_port = decrypted_data.AccountIP_Port.split(":")

    # Create auth token
    auth_token = await xAuThSTarTuP(int(target), token, int(timestamp), key, iv)
    
    await equie_emote(token, url)

    # Start connections
    ready_event = asyncio.Event()
    
    chat_task = asyncio.create_task(
        TcPChaT(chat_ip, chat_port, auth_token, key, iv, 
                decrypted_data, ready_event, region)
    )
    
    await ready_event.wait()
    await asyncio.sleep(1)
    
    online_task = asyncio.create_task(
        TcPOnLine(online_ip, online_port, key, iv, auth_token)
    )

    # Start Flask
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    os.system('clear')
    print(render('BOT', colors=['green', 'white'], align='center'))
    print(f"\n✅ Bot Online | Target: {target}")
    print(f"📡 Region: {region}")
    print(f"🌐 Flask API: http://0.0.0.0:{os.environ.get('PORT', 10000)}")
    print("\n📌 Use: /join?tc=CODE&uid1=UID&emote_id=ID")

    await asyncio.gather(chat_task, online_task)

async def StarTinG():
    while True:
        try:
            await asyncio.wait_for(MaiiiinE(), timeout=7 * 60 * 60)
        except asyncio.TimeoutError:
            print("Token expired, restarting...")
        except Exception as e:
            print(f"Error: {e}, restarting...")
        await asyncio.sleep(5)

# ============= RUN =============
if __name__ == '__main__':
    asyncio.run(StarTinG())