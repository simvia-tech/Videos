# Webinar Qarnot x Kitware x Simvia : Break down the HPC barriers - Making numerical simulation a commodity

## Context

On October 14, Simvia teamed up with Kitware and Qarnot for a hands-on webinar showcasing how open-source tools and cloud-based workflows can overcome traditional HPC limitations—without sacrificing performance.

During the session, participants saw:
- A live demo of a real CFD case using **code_saturne**, the open-source tool developed by EDF R&D, deployed in just a few clicks.
- Interactive post-processing with ParaView through a virtual desktop interface (VDI).
- Immediate access to the test case, enabling attendees to run it on their own.

The provided markdown from the session includes all the technical steps needed to launch the same computations and replicate the full workflow shown during the demo.

## Running the Simulation on Qarnot Platform

This guide explains how to launch the **Blade** simulation on [Qarnot](https://app.qarnot.com), using either the **web platform** or the **Python SDK**.

---

## 🧭 Approach 1 — Using the Qarnot Web Platform

1. **Log in** to your [Qarnot account](https://app.qarnot.com/).

2. **Create a new storage bucket**  
   - Go to the **Storage** section.  
   - From the side menu on the left, open the folders explorer and click **Create folder**, and name it (for example `my-folder`).

3. **Upload the Blade case folder**  
   - Upload the entire `Blade/` directory into your folder.  
   - Make sure the directory structure is preserved.

3. **Upload the Blade case folder**  
   - Upload the entire `Blade/` directory into your folder.  
   - Make sure the directory structure is preserved.

4. **Create and configure your HPC task**
   - Go to the **My simulations** section.  
   - Click **Start a Simulation**, and select **Code_saturne**.  
   - In the next configuration page, select your folder `my-folder`and set the following the following input directory name:
     ```
     Input_directory_name=Blade
     ```
   NB: if you upload the blade directory from the form submission, its contente will be uploaded at the root of your folder (without the blade directory). In that case, change the input directory name to :  
     ```
     Input_directory_name=./
     ``` 
   - Select your pricing plan and hardware. 

5. **Launch the task**
   - Click **Start**.  
   - Once finished, your results will be available in the same folder.

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
