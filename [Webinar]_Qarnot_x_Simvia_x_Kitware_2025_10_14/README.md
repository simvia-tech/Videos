# Webinar Qarnot x Kitware x Simvia : Break down the HPC barriers - Making numerical simulation a commodity

## Context

On October 14, Simvia teamed up with Kitware and Qarnot for a hands-on webinar showcasing how open-source tools and cloud-based workflows can overcome traditional HPC limitations—without sacrificing performance.

During the session, participants saw:
- A live demo of a real CFD case using **code_saturne**, the open-source tool developed by EDF R&D, deployed in just a few clicks.
- Interactive post-processing with ParaView through a virtual desktop interface (VDI).
- Immediate access to the test case, enabling attendees to run it on their own.

The provided markdown from the session includes all the technical steps needed to launch the same computations and replicate the full workflow shown during the demo.

## Running the Simulation on Qarnot Platform

This guide explains how to launch the **Blade** simulation on [Qarnot](https://qarnot.com), using either the **web platform** or the **Python SDK**.

---

## 🧭 Approach 1 — Using the Qarnot Web Platform

1. **Log in** to your [Qarnot account](https://console.qarnot.com/).

2. **Create a new storage bucket**  
   - Go to the **Storage** section.  
   - Click **Create bucket**, and name it (for example `my-bucket`).

3. **Upload the Blade case folder**  
   - Upload the entire `Blade/` directory into your bucket.  
   - Make sure the directory structure is preserved.

4. **Create and configure your HPC task**
   - Go to the **Compute** section.  
   - Click **New Task**, and select the appropriate **Qarnot HPC image** (e.g., your custom simulation image).  
   - In the configuration, set the following environment variable:
     ```
     CS_CASE_NAME=Blade
     ```
   - Select your bucket as input/output storage.  

5. **Launch the task**
   - Click **Run**.  
   - Once finished, your results will be available in the same bucket.

---

## 🐍 Approach 2 — Using the Python SDK

**Install the Qarnot SDK**

```bash
$ pip install qarnot
```
Create a .env file in your working directory with your credentials:

```
QARNOT_USERNAME=your_email@example.com
QARNOT_API_KEY=your_api_key_here
QARNOT_REGISTRY_KEY=your_registry_key_here
```

Run the Python script

```
$ python submit_computation.py
```

The script will:

- Create and configure a Qarnot task.
- Upload the Blade/ folder automatically.
- Submit the task 
