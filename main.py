from pytube import YouTube


def download_youtube_video(url, output_path='C:\\Users\\erik\\Downloads'):
    try:
        print("Membuat objek YouTube...")
        yt = YouTube(url)
        print("Mendapatkan stream video dengan resolusi tertinggi...")
        stream = yt.streams.get_highest_resolution()
        print(f"Mengunduh video ke lokasi: {output_path}")
        stream.download(output_path=output_path)
        print(f"Video '{yt.title}' telah berhasil diunduh.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ").strip()
    output_path = 'C:\\Users\\erik\\Downloads'
    download_youtube_video(url, output_path)
