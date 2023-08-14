import speedtest

def run_speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 10**6  # Convert to Mbps
    upload_speed = st.upload() / 10**6  # Convert to Mbps

    return download_speed, upload_speed

def main():
    print("Welcome to Speed Test Bot!")
    print("Measuring your internet speeds...")

    download_speed, upload_speed = run_speed_test()

    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

if __name__ == "__main__":
    main()
