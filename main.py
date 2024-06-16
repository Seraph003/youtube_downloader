import shutil
from pytube import YouTube

def download_and_move_youtube_video(url, output_path, move_to_path):
    try:
        #Unduh
        print("...")
        yt = YouTube(url)
        print("Mendapatkan video...")
        stream = yt.streams.get_highest_resolution()
        print(f"Mengunduh video ke lokasi: {output_path}")
        video_file = stream.download(output_path=output_path)
        print(f"Video '{yt.title}' telah berhasil diunduh ke {output_path}")

        #Pemindahan lokasi file
        print(f"Memindahkan video ke: {move_to_path}")
        shutil.move(video_file, move_to_path)
        print(f"Video '{yt.title}' berhasil dipindahkan ke {move_to_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    url = input("Masukkan URL video YouTube: ").strip()
    output_path = '.'  #Lokasi path sementara untuk unduhan
    move_to_path = 'C:\\Users\\erik\\Downloads'  #Path akhir
    download_and_move_youtube_video(url, output_path, move_to_path)
