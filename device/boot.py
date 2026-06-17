import subprocess

print("Device Power On")

result = subprocess.run(
    [
        "openssl",
        "dgst",
        "-sha256",
        "-verify",
        "../scripts/public.pem",
        "-signature",
        "../scripts/firmware.sig",
        "../firmware/firmware.bin"
    ],
    capture_output=True,
    text=True
)

if "Verified OK" in result.stdout:
    print("Firmware Verified")
    print("Boot Successful")
else:
    print("Firmware Tampered")
    print("Boot Blocked")
