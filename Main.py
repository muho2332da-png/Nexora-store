<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexora Store | Digital Marketplace</title>
    <style>
        :root { --main-color: #ff0000; --bg-dark: #0a0a0a; --card-bg: #161616; }
        body { background-color: var(--bg-dark); color: white; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; }
        
        /* Header & Logo */
        .header { background: #111; padding: 25px; text-align: center; border-bottom: 2px solid var(--main-color); box-shadow: 0 0 20px rgba(255,0,0,0.2); }
        .logo { font-size: 28px; font-weight: 900; letter-spacing: 4px; color: var(--main-color); text-shadow: 2px 2px 5px black; }

        /* Kategori Slotları */
        .categories { display: flex; overflow-x: auto; padding: 20px; gap: 15px; scrollbar-width: none; }
        .cat-item { min-width: 90px; background: var(--card-bg); padding: 15px; border-radius: 15px; text-align: center; border: 1px solid #222; transition: 0.3s; }
        .cat-item:hover { border-color: var(--main-color); }

        /* Ürün Kartları */
        .container { padding: 15px; display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }
        .product-card { background: var(--card-bg); border-radius: 18px; padding: 12px; border: 1px solid #222; text-align: center; }
        .product-card img { width: 100%; border-radius: 12px; margin-bottom: 10px; border: 1px solid #333; }
        .price { color: #00ff00; font-size: 18px; font-weight: bold; margin: 8px 0; }
        .buy-btn { background: var(--main-color); color: white; border: none; width: 100%; padding: 12px; border-radius: 10px; font-weight: bold; cursor: pointer; transition: 0.2s; }
        .buy-btn:active { transform: scale(0.95); }

        /* Ödeme Modalı (Gizli Form) */
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); z-index: 1000; justify-content: center; align-items: center; }
        .modal-content { background: #1a1a1a; padding: 25px; border-radius: 20px; width: 85%; border: 1px solid var(--main-color); }
        input { width: 100%; padding: 12px; margin: 10px 0; border-radius: 8px; border: 1px solid #333; background: #000; color: white; box-sizing: border-box; }
        .wallet-box { background: #000; padding: 10px; border: 1px dashed var(--main-color); font-size: 11px; word-break: break-all; margin: 10px 0; color: #ccc; }
    </style>
</head>
<body>

    <div class="header">
        <div class="logo">NEXORA</div>
        <div style="font-size: 10px; color: #888; margin-top: 5px;">PREMIUM DIGITAL GOODS</div>
    </div>

    <div class="categories">
        <div class="cat-item">🚗<br><small>Cars</small></div>
        <div class="cat-item">🔑<br><small>Accounts</small></div>
        <div class="cat-item">💰<br><small>Coins</small></div>
        <div class="cat-item">🛡️<br><small>Services</small></div>
    </div>

    <div class="container">
        <div class="product-card">
            <img src="https://via.placeholder.com/300x200/111/ff0000?text=CPM2+CAR" alt="Ürün">
            <div style="font-size: 14px;">BMW M2 FULL MOD</div>
            <div class="price">15.00 USDT</div>
            <button class="buy-btn" onclick="openModal('BMW M2 FULL MOD', '15.00')">SATIN AL</button>
        </div>

        <div class="product-card">
            <img src="https://via.placeholder.com/300x200/111/ff0000?text=CPM2+ACCOUNT" alt="Ürün">
            <div style="font-size: 14px;">CPM2 VIP ACCOUNT</div>
            <div class="price">45.00 USDT</div>
            <button class="buy-btn" onclick="openModal('CPM2 VIP ACCOUNT', '45.00')">SATIN AL</button>
        </div>
    </div>

    <div id="paymentModal" class="modal">
        <div class="modal-content">
            <h3 id="modalTitle" style="margin-top: 0; color: var(--main-color);">Ödeme Yap</h3>
            <p style="font-size: 12px;">Aşağıdaki adrese ödemeyi gönderin ve formu doldurun:</p>
            
            <div class="wallet-box" id="walletAddr">
                TAuNiyKUJEvXqdXAKJ4tkG2nHk23pQW1Qq
            </div>

            <input type="text" id="orderID" placeholder="Oyun ID / Kullanıcı Adı">
            <input type="text" id="contact" placeholder="Telegram Kullanıcı Adınız">
            <input type="text" id="txid" placeholder="Ödeme Dekont No / TXID">
            
            <button class="buy-btn" onclick="sendOrder()">ÖDEMEYİ YAPTIM</button>
            <button style="background:none; color: #555; border:none; width:100%; margin-top:10px;" onclick="closeModal()">İptal Et</button>
        </div>
    </div>

    <script>
        let currentProduct = "";
        let currentPrice = "";

        function openModal(name, price) {
            currentProduct = name;
            currentPrice = price;
            document.getElementById('modalTitle').innerText = name + " - " + price + " USDT";
            document.getElementById('paymentModal').style.display = 'flex';
        }

        function closeModal() {
            document.getElementById('paymentModal').style.display = 'none';
        }

        function sendOrder() {
            const orderID = document.getElementById('orderID').value;
            const contact = document.getElementById('contact').value;
            const txid = document.getElementById('txid').value;

            if(!orderID || !contact || !txid) {
                alert("Lütfen tüm alanları doldurun!");
                return;
            }

            // --- TELEGRAM BOT AYARI ---
            const botToken = "8763683246:AAElhj_BmAMGglrI3q2fiddrHvnNHimHKzc";
            const chatID = "-1003878694343";
            const mesaj = `🚨 YENİ SİPARİŞ!\n\n📦 Ürün: ${currentProduct}\n💰 Fiyat: ${currentPrice} USDT\n👤 Müşteri: ${orderID}\n📱 İletişim: ${contact}\n🧾 TXID: ${txid}`;

            const url = `https://api.telegram.org/bot${botToken}/sendMessage?chat_id=${chatID}&text=${encodeURIComponent(mesaj)}`;

            fetch(url).then(res => {
                alert("Sipariş alındı! Ödemeniz onaylandıktan sonra sizinle iletişime geçilecektir.");
                closeModal();
            });
        }
    </script>
</body>
</html>
