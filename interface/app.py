# load libraries
import os
import cv2 as cv
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# helper function
@st.cache
def preds_eye(filename):
	"main function for our testing image"
	img = np.expand_dims(img_to_array(load_img(filename,
	                                           target_size = (512, 512))),
	                     axis = 0)/255
	predicted_result = np.argmax(model.predict(img))
	return predicted_result


# initialization
model = load_model("../model/model_blindness.h5")
label_list = ['normal', 'mild', 'moderate', 'severe', 'proliferate']
preds = 0

# sidebar section
available_options = ["", "Overview", "Symtomps", "Prevention",
                     "Eye Screening", "Retina Detection", "Treatment"]
option = st.sidebar.selectbox("Choose Features :", available_options)
available_img = [i for i in os.listdir(".././example") if i.endswith('.png')]
filename = st.sidebar.selectbox("Choose Example Image :", [""] + available_img)

# main section
if option == 'Overview':
    desc = """
        # Diabetic Retinopathy
        ***
        ## Overview
        Diabetic retinopathy is a complication of diabetes, 
        which is caused by high blood sugar levels damaging the back of the eye (retina). 
        It can lead to blindness if undiagnosed and untreated.
        However, it usually takes several years for diabetic retinopathy to reach a stage that can threaten your vision.
        
        ## How diabetes can affect the eyes ?
        The retina is the light-sensitive layer of cells at the back of the eye 
        that converts light into electrical signals. The signals are sent to the brain 
        which turns them into the images you see.
        The retina needs a constant supply of blood, 
        which it receives through a network of tiny blood vessels. 
        Over time, a persistently high blood sugar level can damage these blood vessels in 3 main stages :
        
          1. **background retinopathy** – tiny bulges develop in the blood vessels, which may bleed slightly but don't usually affect your vision
          2. **pre-proliferative retinopathy** – more severe and widespread changes affect the blood vessels, including more significant bleeding into the eye
          3. **proliferative retinopathy** – scar tissue and new blood vessels, which are weak and bleed easily, develop on the retina, this can result in some loss of vision 
    
        **However, if a problem with your eyes is picked up early, lifestyle changes and/or treatment can stop it getting worse.**   
    """
    st.markdown(desc)

elif option == 'Symtomps':
    desc = """
        # Symptoms of Diabetic Retinopathy
        You won't usually notice diabetic retinopathy in the early stages, 
        as it doesn't tend to have any obvious symptoms until it's more advanced.
        However, early signs of the condition can be picked up by taking photographs of the eyes during diabetic eye screening.
        Contact your GP or diabetes care team immediately if you experience :
          
          1. gradually worsening vision
          2. sudden vision loss
          3. shapes floating in your field of vision (floaters)
          4. blurred or patchy vision
          5. eye pain or redness
          
        **These symptoms don't necessarily mean you have diabetic retinopathy, 
        but it's important to get them checked out. Don't wait until your next screening appointment.**
    """
    st.markdown(desc)
    img_example = cv.imread("static/2.jpg")[:, :, ::-1]
    st.image(img_example)

    desc_2 = """
        # Diabetic retinopathy develops in stages over time
        If you're diagnosed with diabetic retinopathy after diabetic eye screening, 
        lifestyle changes and/or treatment can reduce the chances of the problem progressing.
        The main stages of diabetic retinopathy are described below. You won't necessarily experience all of these.
        
        ## Stage 1: background retinopathy
        This means that tiny bulges (microaneurysms) have appeared in the blood vessels in the back of your eyes (retina), 
        which may leak small amounts of blood. This is very common in people with diabetes. At this stage :
        
          1. your sight isn't affected, although you're at a higher risk of developing vision problems in the future
          2. you don't need treatment, but you'll need to take care to prevent the problem getting worse
          3. the chances of it progressing to the stages below within 3 years are more than 25% if both of your eyes are affected
          
        ## Stage 2: pre-proliferative retinopathy
        This means that more severe and widespread changes are seen in the retina, 
        including bleeding into the retina. At this stage :
        
          1. there's a high risk that your vision could eventually be affected
          2. you'll usually be advised to have more frequent screening appointments every 3 to 6 months to monitor your eyes
          
        ## Stage 3: proliferative retinopathy
        This means that new blood vessels and scar tissue have formed on your retina, 
        which can cause significant bleeding and lead to retinal detachment 
        (where the retina pulls away from the back of the eye). At this stage :
        
        1. There's a very high risk you could lose your vision
        2. Treatment will be offered to stabilise your vision as much as possible, although it won't be possible to restore any vision you've lost
        
        # Diabetic eye screening
        Everyone with diabetes who is 12 years old or over is invited for eye screening once a year. Screening is offered because :
        
        1. Diabetic retinopathy doesn't tend to cause any symptoms in the early stages
        2. The condition can cause permanent blindness if not diagnosed and treated promptly
        3. Screening can detect problems in your eyes before they start to affect your vision
        4. If problems are caught early, treatment can help prevent or reduce vision loss
        
        The screening test involves examining the back of the eyes and taking photographs. 
        Depending on your result, you may be advised to return for another appointment a year later, 
        attend more regular appointments, or discuss treatment options with a specialist.
        
        # Which stage am I at?
        If you've had a diabetic eye screening test, you'll be sent a letter stating that you have one of the following:
         
        1. **no retinopathy** – this means no signs of retinopathy were found and you should attend your next screening appointment in 12 months
        2. **background retinopathy** – this means you have stage 1 retinopathy and should attend your next screening appointment in 12 months
        3. **degrees of referable retinopathy** – this means you have stage 2 or 3 retinopathy, or diabetic maculopathy, and should have more frequent tests or talk to a specialist about possible treatments
    """
    st.markdown(desc_2)
    img_example = cv.imread("static/3.jpg")[:, :, ::-1]
    st.image(img_example)

elif option == "Prevention":
    desc = """
        # Reduce Risk of Diabetic Retinopathy
        You can reduce your risk of developing diabetic retinopathy, 
        or help stop it getting worse, by keeping your blood sugar levels, 
        blood pressure and cholesterol levels under control.
        This can often be done by making healthy lifestyle choices, although some people will also need to take medication.
        
        ## Healthy lifestyle
        Adopting a few lifestyle changes can improve your general health and reduce your risk of developing retinopathy. These include :
        
          1. Eating a healthy, balanced diet – in particular, try to cut down on salt, fat and sugar
          2. Losing weight if you're overweight – you should aim for a BMI of 18.5-24.9; use the BMI calculator to work out your BMI
          3. Exercising regularly – aim to do at least 150 minutes of moderate-intensity activity, such as walking or cycling, a week; doing 10,000 steps a day can be a good way to reach this target
          4. Stopping smoking if you smoke
          5. Not exceeding the recommended alcohol limits – men and women are advised not to regularly drink more than 14 alcohol units a week
          
        You may also be prescribed medication to help control your blood sugar level (such as insulin or metformin), 
        blood pressure (such as ACE inhibitors) and/or cholesterol level (such as statins).
    
        ## Know your blood sugar, blood pressure and cholesterol levels
        It can be easier to keep your blood sugar levels, blood pressure and cholesterol levels under control if you monitor them regularly and know what level they are.
        The lower you can keep them, the lower your chances of developing retinopathy are. Your diabetes care team can let you know what your target levels should be.
          
          1. Blood sugar
          If you check your blood sugar level at home, it should be 4 to 10mmol/l. The level can vary throughout the day, so try to check it at different times.
          The check done at your GP surgery is a measure of your average blood sugar level over the past few weeks. You should know this number, as it is the most important measure of your diabetes control. 
          It's called HbA1c, and for most people with diabetes it should be around 48mmol/l or 6.5%.
          
          2. Blood pressure
          You can ask for a blood pressure test at your GP surgery, or you can buy a blood pressure monitor to use at home. Blood pressure is measured in millimetres of mercury (mmHg) and is given as 2 figures.
          If you have diabetes, you'll normally be advised to aim for a blood pressure reading of no more than 140/80mmHg, or less than 130/80mmHg if you have diabetes complications, such as eye damage.
          
          3. Cholesterol
          Your cholesterol level can be measured with a simple blood test carried out at your GP surgery. The result is given in millimoles per litre of blood (mmol/l).
          If you have diabetes, you'll normally be advised to aim for a total blood cholesterol level of no more than 4mmol/l.
          
          4. Regular screening
          Even if you think your diabetes is well controlled, it's still important to attend your annual diabetic eye screening appointment, as this can detect signs of a problem before you notice anything is wrong.
          Early detection of retinopathy increases the chances of treatment being effective and stopping it getting worse.
          You should also contact your GP or diabetes care team immediately if you develop any problems with your eyes or vision, such as:
          
            * Gradually worsening vision
            * Sudden vision loss
            * Shapes floating in your field of vision (floaters)
            * Blurred vision
            * Eye pain or redness
    """
    st.markdown(desc)

elif option == "Eye Screening":
    desc = """
        # What is Diabetic Eye Screening ?
          1. Diabetic eye screening is a test to check for eye problems caused by diabetes.
          2. Eye problems caused by diabetes are called diabetic retinopathy. This can lead to sight loss if it's not found early.
          3. The eye screening test can find problems before they affect your sight.
          4. Pictures are taken of the back of your eyes to check for any changes.
          5. If you have diabetes and you're aged 12 or over, you'll get a letter asking you to have your eyes checked at least once a year.
    """
    st.markdown(desc)
    img_example = cv.imread("static/5.jpg")[:, :, ::-1]
    st.image(img_example)

elif option == "Retina Detection":
    st.title("Retection Apps")
    if filename != "":
        name = filename.split(".")[0]
        img = cv.resize(cv.imread("../example/" + filename), (350, 250))
        col1, col2, col3 = st.columns([23, 20, 13])
        col2.write(f"ID : {name}")
        col1, col2, col3 = st.columns([10, 20, 10])
        col2.image(img[:, :, ::-1])

        col1, col2, col3 = st.columns([20, 10, 15])
        if col2.button('predict'):
            with st.spinner("Please Wait..."):
                predicted_label = preds_eye("../example/" + filename)
                preds = predicted_label
                st.success(f"Predicted Label Is : {label_list[predicted_label]}")
                st.balloons()
        # suggestion here - not added / found ~

elif option == "Treatment":
    desc = """
        # Managing your diabetes
        
        The most important part of your treatment is to keep your diabetes under control.
        In the early stages of diabetic retinopathy, controlling your diabetes can help prevent vision problems developing.
        In the more advanced stages, when your vision is affected or at risk, keeping your diabetes under control can help stop the condition getting worse.
        
        # Treatments for advanced diabetic retinopathy
        For diabetic retinopathy that is threatening or affecting your sight, the main treatments are :
        
         1. **laser treatment** – to treat the growth of new blood vessels at the back of the eye (retina) in cases of proliferative diabetic retinopathy, and to stabilise some cases of maculopathy
         2. **eye injections** – to treat severe maculopathy that's threatening your sight
         3. **eye surgery** – to remove blood or scar tissue from the eye if laser treatment isn't possible because retinopathy is too advanced
         
        ## Laser treatment
        Laser treatment is used to treat new blood vessels at the back of the eyes in the advanced stages of diabetic retinopathy. 
        This is done because the new blood vessels tend to be very weak and often cause bleeding into the eye.
        Treatment can help stabilise the changes in your eyes caused by your diabetes and stop your vision getting any worse, 
        although it won't usually improve your sight.
        
        ### Laser treatment :
         1. involves shining a laser into your eyes – you'll be given local anaesthetic drops to numb your eyes; eye drops are used to widen your pupils and special contact lenses are used to hold your eyelids open and focus the laser onto your retina
         2. normally takes around 20-40 minutes
         3. is usually carried out on an outpatient basis, which means you won't need to stay in hospital overnight
         4. may require more than one visit to a laser treatment clinic
         5. isn't usually painful, although you may feel a sharp pricking sensation when certain areas of your eye are being treated
         
        ### Side effects
        After treatment, you may have some side effects for a few hours. These can include :

         1. Blurred vision – you won't be able to drive until this passes, so you'll need to arrange for a friend or relative to drive you home, or take public transport
         2. Increased sensitivity to light – it might help to wear sunglasses until your eyes have adjusted
         3. Aching or discomfort – over-the-counter painkillers, such as paracetamol, should help

        ### Possible complications
        You should be told about the risks of treatment in advance. Potential complications include :
        
         1. Reduced night or peripheral (side) vision – some people may have to stop driving as a result of this
         2. Bleeding into the eye or objects floating in your vision (floaters)
         3. being able to "see" the pattern made by the laser on the back of your eye for a few months
         4. a small, but permanent, blind spot close to the centre of your vision
         
        **Get medical advice if you notice that your sight gets worse after treatment.**
        
        ## Eye injections
        In some cases of diabetic maculopathy, injections of a medicine called anti-VEGF may be given directly into your eyes to prevent new blood vessels forming at the back of the eyes.
        The main medicines used are called ranibizumab (Lucentis) and aflibercept (Eylea). These can help stop the problems in your eyes getting worse, and may also lead to an improvement in your vision.
        During treatment:
        
         1. The skin around your eyes will be cleaned and covered with a sheet
         2. Small clips will be used to keep your eyes open
         3. You'll be given local anaesthetic drops to numb your eyes
         4. A very fine needle is carefully guided into your eyeball and the injection is given
        
        The injections are usually given once a month to begin with. Once your vision starts to stabilise, they'll be stopped or given less frequently.
        
        ### Risks and side effects
        Possible risks and side effects of anti-VEGF injections include:
         
         1. Eye irritation or discomfort
         2. Bleeding inside the eyw
         3. Floaters or a feeling of having something in your eye
         4. Watery or dry, itchy eyes
         5. There's also a risk that the injections could cause blood clots to form, which could lead to a heart attack or stroke. This risk is small, but it should be discussed with you before you give your consent to treatment.
         
        **The main risk with steroid injections is increased pressure inside the eye.**
        
        ## Eye surgery
        Surgery may be carried out to remove some of the vitreous humour from the eye. This is the transparent, 
        jelly-like substance that fills the space behind the lens of the eye.
        The operation, known as vitreoretinal surgery, may be needed if:
        
         1. a large amount of blood has collected in your eye
         2. there's extensive scar tissue that's likely to cause, or has already caused, retinal detachment
         
        During the procedure, the surgeon will make a small incision in your eye before removing some of the vitreous humour, removing any scar tissue and using a laser to prevent a further deterioration in your vision.
        Vitreoretinal surgery is usually carried out under local anaesthetic and sedation. This means you will not experience any pain or have any awareness of the surgery being performed.
        
        ### After the procedure
        You should be able to go home on the same day or the day after your surgery.
        For the first few days, you may need to wear a patch over your eye. This is because activities such as reading and watching television can quickly tire your eye to begin with.
        You will probably have blurred vision after the operation. This should improve gradually, although it may take several months for your vision to fully return to normal.
        Your surgeon will advise you about any activities you should avoid during your recovery.
        
        ### Risks and side effects
        Possible risks of vitreoretinal surgery include:
        
         1. Developing a cataract
         2. Further bleeding into the eye
         3. Retinal detachment
         4. Fluid build-up in the cornea (outer layer at the front of the eye)
         5. infection in the eye
         
        **There's also a small chance that you will need further retinal surgery afterwards. Your surgeon will explain the risks to you.**
    """
    st.markdown(desc)

else:
    # main bar section
    st.title("Retection Apps")
    description = """
    Retection is a system  to detect the scale 
    of blindness on the retina based on the image then the results 
    of the prediction will display the type of classification on a 
    scale of 0 - 4 and preventive and treatment measures that can 
    maintain eye health.
    	"""
    st.write(description)
    img_example = cv.imread("static/1.jpeg")[:, :, ::-1]
    st.image(img_example)