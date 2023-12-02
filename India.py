import subprocess

# Install Playwright using pip
subprocess.run(["pip", "install", "playwright"])

# Install Playwright dependencies
subprocess.run(["playwright", "install"])

# Run 'playwright install-deps' using subprocess.run
subprocess.run(["playwright", "install-deps"])

# Install getindianname using pip
subprocess.run(["pip", "install", "indian_names"])
