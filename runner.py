import subprocess
import sys
import time

def run_spotdl(url):
    command = [sys.executable, "-m", "spotdl", url]

    while True:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        stdout_lines = []
        stderr_lines = []

        try:
            for stdout_line in iter(process.stdout.readline, ""):
                stdout_lines.append(stdout_line)
                print(stdout_line, end="")
                if "AudioProviderError" in stdout_line or "OSError" in stdout_line or "SpotifyException" in stdout_line:
                    print("Fatal error detected in stdout. Retrying in 5 seconds...")
                    time.sleep(5)
                    break

            for stderr_line in iter(process.stderr.readline, ""):
                stderr_lines.append(stderr_line)
                print(stderr_line, end="")
                if "AudioProviderError" in stderr_line or "OSError" in stderr_line or "SpotifyException" in stderr_line:
                    print("Fatal error detected in stderr. Retrying in 5 seconds...")
                    time.sleep(5)
                    break

        except Exception as e:
            print(f"Error: {e}")

        process.stdout.close()
        process.stderr.close()
        process.wait()

        stdout = ''.join(stdout_lines)
        stderr = ''.join(stderr_lines)

        if process.returncode == 0:
            print("Command ran successfully!")
            return
        else:
            print("Error detected. Retrying in 5 seconds...")
            time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <spotify_url>")
        sys.exit(1)

    playlist_url = sys.argv[1]
    run_spotdl(playlist_url)
