from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
================================================================================
USER MANUAL: SMART HOME SECURITY SYSTEM (MODEL X-500)
================================================================================

1. INITIAL HARDWARE SETUP
- Step 1: Unpack the primary control hub and connect the power adapter.
- Step 2: Insert the backup lithium-ion battery into the bottom compartment.
- Step 3: Connect the hub to your local Wi-Fi network using the mobile application.
- Step 4: Mount motion sensors at least 7 feet above floor level for optimal range.

2. SYSTEM CONFIGURATION & NETWORK SETTINGS
* Network Protocol: WPA3 Enforced (2.4 GHz required for sensor pairing)
* IP Assignment: Static IP recommended for home automation hubs
* Firmware Updates: Automatic checks occur daily at 03:00 AM
* Primary Contact Number: Enter up to 3 emergency notification numbers

3. SENSOR SPECIFICATIONS & OPERATING MODES

Mode: AWAY
- Motion Detectors: ACTIVE (High Sensitivity)
- Door / Window Sensors: ACTIVE
- Glass Break Sensors: ACTIVE
- Camera Streaming: CONTINUOUS RECORDING (1080p, 30fps)

Mode: HOME / STAY
- Motion Detectors: DISABLED (Prevents false alarms from indoor movement)
- Door / Window Sensors: ACTIVE
- Glass Break Sensors: ACTIVE
- Camera Streaming: EVENT-TRIGGERED ONLY

Mode: OFF / DISARMED
- Motion Detectors: DISABLED
- Door / Window Sensors: DISABLED
- Panic Button: ALWAYS ACTIVE (24/7 Monitoring)
- Smoke / Carbon Monoxide Detectors: ALWAYS ACTIVE

4. TROUBLESHOOTING & ERROR CODES
[ERR-101] WiFi Disconnected -> Restart router and verify 2.4 GHz band visibility.
[ERR-204] Sensor Battery Low -> Replace CR2032 coin cell within 48 hours.
[ERR-309] Hub Tamper Warning -> Ensure baseplate is securely locked in place.
[ERR-400] Firmware Sync Fail -> Factory reset hub by holding red button for 10s.

5. MAINTENANCE CHECKLIST
- Monthly: Perform walk-test to verify sensor detection ranges.
- Quarterly: Clean camera lenses with microfiber cloth (do not use solvents).
- Semi-Annually: Test emergency siren sound levels (minimum 85 dB at 10 feet).
- Annually: Replace backup battery unit in the main control panel.
================================================================================
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)