<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Adresi Doğrulama Hizmeti</title>
    <!-- Tailwind CSS'i CDN üzerinden dahil ediyoruz -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Font Awesome ikonlarını ekliyoruz -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        body {
            font-family: 'Inter', sans-serif;
            background-color: #1a202c; /* Koyu arka plan */
        }
    </style>
</head>
<body class="bg-gray-900 text-white flex items-center justify-center min-h-screen p-4">
    <div class="container mx-auto p-4 md:p-8">
        <!-- İlk Ekran: Başlangıç ve Buton -->
        <div id="baslangic-ekrani" class="text-center transition-opacity duration-1000 ease-in-out">
            <h1 class="text-3xl md:text-5xl font-bold mb-4 text-white">IP Adresi Doğrulama Servisi</h1>
            <p class="text-md md:text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
                Sisteminizin güvenliğini sağlamak için IP adresinizi doğrulayın. Bu işlem, hesabınızı korumak için gereklidir.
            </p>
            <button id="baslat-butonu" class="bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-all duration-300 transform hover:scale-105">
                <i class="fa-solid fa-shield-halved mr-2"></i> Doğrulamayı Başlat
            </button>
        </div>

        <!-- İkinci Ekran: Yükleme ve Sonuç -->
        <div id="dogrulama-ekrani" class="hidden opacity-0 text-center transition-opacity duration-1000 ease-in-out">
            <h2 class="text-2xl md:text-4xl font-bold mb-6 text-yellow-400 animate-pulse">IP Doğrulama İşlemi Başlatıldı...</h2>
            
            <!-- Yükleme Çubuğu -->
            <div class="w-full max-w-2xl mx-auto bg-gray-700 rounded-full h-4 mb-4">
                <div id="progress-bar" class="bg-yellow-500 h-4 rounded-full transition-all duration-500 ease-in-out" style="width: 0%;"></div>
            </div>
            
            <!-- Log Akışı -->
            <div id="log-akisi" class="text-left bg-gray-800 p-4 rounded-lg h-64 overflow-y-scroll font-mono text-sm text-gray-400 max-w-2xl mx-auto">
                <p>> Bağlantı kuruluyor... <span class="text-green-500">[OK]</span></p>
                <p>> IP adresi tespiti: 192.168.1.1 <span class="text-green-500">[OK]</span></p>
            </div>

            <!-- Şaka Sonucu -->
            <div id="sonuc-icerik" class="hidden text-center mt-8">
                <h3 class="text-4xl md:text-6xl font-bold mb-4 text-green-500">Tebrikler!</h3>
                <p class="text-xl md:text-2xl mb-8 text-white">
                    IP adresin başarıyla doğrulandı. yaramı ye şimdi jqwhejqwheqh
                </p>
                <img
                    src="https://media.giphy.com/media/l4pTfx2qLsQakm0MM/giphy.gif"
                    alt="Komik kedi gif"
                    class="mx-auto rounded-lg shadow-xl"
                    onerror="this.src='https://placehold.co/480x270/2d2d2d/ffffff?text=Resim+Yüklenemedi'"
                />
            </div>
        </div>
    </div>

    <script>
        const baslatButonu = document.getElementById('baslat-butonu');
        const baslangicEkrani = document.getElementById('baslangic-ekrani');
        const dogrulamaEkrani = document.getElementById('dogrulama-ekrani');
        const progressBar = document.getElementById('progress-bar');
        const logAkisi = document.getElementById('log-akisi');
        const sonucIcerik = document.getElementById('sonuc-icerik');

        const logMesajlari = [
            "Güvenlik sertifikaları kontrol ediliyor... [OK]",
            "Güvenlik duvarı parametreleri taranıyor... [OK]",
            "Kötü amaçlı yazılım imzaları güncelleniyor... [OK]",
            "Veri paketleri analiz ediliyor... [OK]",
            "Bağlantı noktası protokolleri kontrol ediliyor... [OK]",
            "Sistem güvenlik puanı hesaplanıyor... [OK]",
            "Sonuçlar hazırlanıyor... [OK]",
            "Doğrulama tamamlandı... [OK]"
        ];

        let logIndex = 0;
        let progress = 0;
        let intervalId;

        function updateProgress() {
            if (progress < 100) {
                progress += Math.floor(Math.random() * 5) + 5;
                if (progress > 100) progress = 100;
                progressBar.style.width = `${progress}%`;
                
                // Belirli aralıklarla yeni log mesajı ekle
                if (logIndex < logMesajlari.length && progress > (logIndex * (100 / logMesajlari.length))) {
                    const yeniLog = document.createElement('p');
                    yeniLog.textContent = `> ${logMesajlari[logIndex]}`;
                    logAkisi.appendChild(yeniLog);
                    logAkisi.scrollTop = logAkisi.scrollHeight; // En alta kaydır
                    logIndex++;
                }

                if (progress < 100) {
                    setTimeout(updateProgress, 200);
                } else {
                    clearInterval(intervalId);
                    setTimeout(() => {
                        sonucIcerik.classList.remove('hidden');
                        sonucIcerik.classList.add('animate-fadeIn');
                    }, 1500); // Sonucu göstermeden önce 1.5 saniye bekle
                }
            }
        }

        baslatButonu.addEventListener('click', () => {
            baslangicEkrani.classList.add('opacity-0');
            setTimeout(() => {
                baslangicEkrani.classList.add('hidden');
                dogrulamaEkrani.classList.remove('hidden');
                setTimeout(() => {
                    dogrulamaEkrani.classList.add('opacity-100');
                    updateProgress(); // Yükleme işlemini başlat
                }, 50);
            }, 1000);
        });
    </script>
</body>
</html>
