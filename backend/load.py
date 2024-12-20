from owlready2 import *

# File name for the ontology
FILE_NAME = "anatomy.owl"

# Create or load the ontology
onto = get_ontology(f"http://www.example.org/{FILE_NAME}")

with onto:
    # Define the Organs class as a subclass of Anatomy
    class Organs(Thing):
        pass

    # Define the System class as a subclass of Anatomy
    class System(Thing):
        pass

    # Define ObjectProperties
    class isPartOf(ObjectProperty):
        domain = [Organs]
        range = [System]
        label = "Is part of"

    # Define DatatypeProperties for Organs
    class latin(DataProperty, FunctionalProperty):
        domain = [Organs]
        range = [str]

    class mainFunction(DataProperty, FunctionalProperty):
        domain = [Organs]
        range = [str]

    # Define DatatypeProperties for Systems
    class description(DataProperty, FunctionalProperty):
        domain = [System]
        range = [str]

    class label(DataProperty, FunctionalProperty):
        domain = [System]
        range = [str]

    # JSON data for systems
    systems_data = [
    {"name": "SkeletalSystem", "label": "Skeletal System", "description": "The skeletal system includes all of the bones and joints in the body. Each bone is a complex living organ that is made up of many cells, protein fibers, and minerals. The skeleton acts as a scaffold by providing support and protection for the soft tissues that make up the rest of the body. The skeletal system also provides attachment points for muscles to allow movements at the joints. New blood cells are produced by the red bone marrow inside of our bones. Bones act as the body's warehouse for calcium, iron, and energy in the form of fat. Finally, the skeleton grows throughout childhood and provides a framework for the rest of the body to grow along with it."},
    {"name": "MuscularSystem", "label": "Muscular System", "description": "The muscular system is responsible for the movement of the human body. Attached to the bones of the skeletal system are about 700 named muscles that make up roughly half of a person's body weight. Each of these muscles is a discrete organ constructed of skeletal muscle tissue, blood vessels, tendons, and nerves. Muscle tissue is also found inside of the heart, digestive organs, and blood vessels. In these organs, muscles serve to move substances throughout the body."},
    {"name": "CardiovascularSystem", "label": "Cardiovascular System", "description": "The cardiovascular system consists of the heart, blood vessels, and the approximately 5 liters of blood that the blood vessels transport. Responsible for transporting oxygen, nutrients, hormones, and cellular waste products throughout the body, the cardiovascular system is powered by the body's hardest-working organ --- the heart, which is only about the size of a closed fist. Even at rest, the average heart easily pumps over 5 liters of blood throughout the body every minute."},
    {"name": "DigestiveSystem", "label": "Digestive System", "description": "The digestive system is a group of organs working together to convert food into energy and basic nutrients to feed the entire body. Food passes through a long tube inside the body known as the alimentary canal or the gastrointestinal tract (GI tract). The alimentary canal is made up of the oral cavity, pharynx, esophagus, stomach, small intestines, and large intestines. In addition to the alimentary canal, there are several important accessory organs that help your body to digest food but do not have food pass through them. Accessory organs of the digestive system include the teeth, tongue, salivary glands, liver, gallbladder, and pancreas."},
    {"name": "EndocrineSystem", "label": "Endocrine System", "description": "The endocrine system includes all of the glands of the body and the hormones produced by those glands. The glands are controlled directly by stimulation from the nervous system as well as by chemical receptors in the blood and hormones produced by other glands. By regulating the functions of organs in the body, these glands help to maintain the body's homeostasis. Cellular metabolism, reproduction, sexual development, sugar and mineral homeostasis, heart rate, and digestion are among the many processes regulated by the actions of hormones."},
    {"name": "NervousSystem", "label": "Nervous System", "description": "The nervous system consists of the brain, spinal cord, sensory organs, and all of the nerves that connect these organs with the rest of the body. Together, these organs are responsible for the control of the body and communication among its parts. The brain and spinal cord form the control center known as the central nervous system (CNS), where information is evaluated and decisions made. The sensory nerves and sense organs of the peripheral nervous system (PNS) monitor conditions inside and outside of the body and send this information to the CNS. Efferent nerves in the PNS carry signals from the control center to the muscles, glands, and organs to regulate their functions."},
    {"name": "RespiratorySystem", "label": "Respiratory System", "description": "The cells of the human body require a constant stream of oxygen to stay alive. The respiratory system provides oxygen to the body's cells while removing carbon dioxide, a waste product that can be lethal if allowed to accumulate. There are 3 major parts of the respiratory system: the airway, the lungs, and the muscles of respiration. The airway, which includes the nose, mouth, pharynx, larynx, trachea, bronchi, and bronchioles, carries air between the lungs and the body's exterior. The lungs act as the functional units of the respiratory system by passing oxygen into the body and carbon dioxide out of the body. Finally, the muscles of respiration, including the diaphragm and intercostal muscles, work together to act as a pump, pushing air into and out of the lungs during breathing."},
    {"name": "LymphaticSystem", "label": "Lymphatic System", "description": "The immune and lymphatic systems are two closely related organ systems that share several organs and physiological functions. The immune system is our body's defense system against infectious pathogenic viruses, bacteria, and fungi as well as parasitic animals and protists. The immune system works to keep these harmful agents out of the body and attacks those that manage to enter.\nThe lymphatic system is a system of capillaries, vessels, nodes and other organs that transport a fluid called lymph from the tissues as it returns to the bloodstream. The lymphatic tissue of these organs filters and cleans the lymph of any debris, abnormal cells, or pathogens. The lymphatic system also transports fatty acids from the intestines to the circulatory system."},
    {"name": "UrinarySystem", "label": "Urinary System", "description": "The urinary system consists of the kidneys, ureters, urinary bladder, and urethra. The kidneys filter the blood to remove wastes and produce urine. The ureters, urinary bladder, and urethra together form the urinary tract, which acts as a plumbing system to drain urine from the kidneys, store it, and then release it during urination. Besides filtering and eliminating wastes from the body, the urinary system also maintains the homeostasis of water, ions, pH, blood pressure, calcium and red blood cells."},
    {"name": "MaleReproductiveSystem", "label": "Male Reproductive System", "description": "The male reproductive system includes the scrotum, testes, spermatic ducts, sex glands, and penis. These organs work together to produce sperm, the male gamete, and the other components of semen. These reproductive organs also work together to deliver semen out of the body and into the vagina where it can fertilize egg cells to produce offspring."},
    {"name": "FemaleReproductiveSystem", "label": "Female Reproductive System", "description": "The female reproductive system includes the ovaries, fallopian tubes, uterus, and vagina. These organs work together to produce eggs, facilitate fertilization, and support fetal development during pregnancy."},
    {"name": "IntegumentarySystem", "label": "Integumentary System", "description": "The integumentary system is an organ system consisting of the skin, hair, nails, and exocrine glands. The skin is only a few millimeters thick yet is by far the largest organ in the body. The average person's skin weighs 10 pounds and has a surface area of almost 20 square feet. Skin forms the body's outer covering and forms a barrier to protect the body from chemicals, disease, UV light, and physical damage. Hair and nails extend from the skin to reinforce the skin and protect it from environmental damage. The exocrine glands of the integumentary system produce sweat, oil, and wax to cool, protect, and moisturize the skin's surface."}
]

    # JSON data for organs
    organs_data = [
    {
        "name": "Heart",
        "latin": "cor",
        "mainFunction": "The heart's primary function is to pump blood throughout the body, ensuring the delivery of oxygen and nutrients to tissues while removing carbon dioxide and waste products. It accomplishes this through two main circulatory pathways: pulmonary circulation, where deoxygenated blood is sent to the lungs to exchange carbon dioxide for oxygen, and systemic circulation, where oxygen-rich blood is distributed to the rest of the body. By maintaining blood pressure and circulating blood through a network of vessels, the heart supports vital metabolic processes and homeostasis. Additionally, it plays a regulatory role by producing hormones like atrial natriuretic peptide (ANP), which help control blood volume and pressure. This efficient and continuous operation is essential for sustaining life and ensuring the proper functioning of all body systems.",
        "system": "CardiovascularSystem"
    },
    {
        "name": "Arteries",
        "latin": "arteriae",
        "mainFunction": "The primary function of arteries is to carry oxygen-rich blood away from the heart to the various tissues and organs of the body, ensuring they receive the oxygen and nutrients necessary for proper function. Arteries have thick, elastic walls that can withstand the high pressure of blood being pumped by the heart, allowing them to maintain a steady flow throughout the circulatory system. They also play a critical role in regulating blood pressure and flow by contracting or relaxing their muscular walls, a process known as vasoconstriction and vasodilation. This adaptability ensures that blood is efficiently delivered to areas with the greatest demand, such as muscles during exercise, while maintaining overall circulatory balance.",
        "system": "CardiovascularSystem"
    },
    {
        "name": "Veins",
        "latin": "venae",
        "mainFunction": "The primary function of veins is to carry deoxygenated blood from the body's tissues back to the heart, where it can be sent to the lungs for reoxygenation. Unlike arteries, veins have thinner walls and lower pressure, but they are equipped with valves that prevent the backflow of blood, ensuring it moves efficiently toward the heart. Veins also play a crucial role in maintaining blood volume and regulating circulation, especially during changes in posture or activity. Through their vast network, veins collect waste-laden blood from tissues, completing the circulatory loop and supporting the body's metabolic needs.",
        "system": "CardiovascularSystem"
    },
    {
        "name": "Lungs",
        "latin": "pulmo",
        "mainFunction": "The primary function of the lungs is to facilitate the exchange of gases between the blood and the external environment, providing oxygen to the bloodstream while removing carbon dioxide. This process, known as respiration, occurs in tiny air sacs called alveoli, where oxygen from inhaled air diffuses into the blood, and carbon dioxide from the blood is expelled into the air to be exhaled. The lungs also help regulate the body's pH by controlling carbon dioxide levels and play a role in filtering small blood clots and air bubbles. Additionally, they produce surfactant, a substance that reduces surface tension in the alveoli, preventing lung collapse and ensuring efficient breathing.",
        "system": "RespiratorySystem"
    },
    {
        "name": "Trachea",
        "latin": "trachea",
        "mainFunction": "The trachea, commonly known as the windpipe, serves as the primary airway that connects the throat (pharynx) and voice box (larynx) to the lungs. Its main function is to provide a clear and secure passage for air to travel to and from the lungs during breathing. The trachea is reinforced with C-shaped cartilage rings that keep it open and prevent collapse while allowing flexibility during movement. It is also lined with a mucous membrane and cilia, which trap and expel dust, debris, and pathogens, protecting the respiratory system from harmful particles. This structure ensures the efficient flow of air and supports respiratory health.",
        "system": "RespiratorySystem"
    },
    {
        "name": "Diaphragm",
        "latin": "diaphragma",
        "mainFunction": "The diaphragm is a dome-shaped muscular structure located at the base of the chest, playing a crucial role in breathing. Its primary function is to facilitate the expansion and contraction of the lungs during respiration. When the diaphragm contracts, it flattens and moves downward, increasing the thoracic cavity's volume and creating a vacuum that draws air into the lungs (inhalation). During relaxation, it moves upward, decreasing the thoracic cavity's volume and pushing air out of the lungs (exhalation). Additionally, the diaphragm assists in actions like coughing, sneezing, and vomiting by exerting pressure on the abdominal cavity. It is a vital muscle for maintaining efficient respiratory function.",
        "system": "RespiratorySystem"
    },
    {
        "name": "Stomach",
        "latin": "ventriculus",
        "mainFunction": "The stomach is a vital organ in the digestive system, primarily responsible for breaking down and digesting food to prepare it for absorption in the intestines. It accomplishes this by secreting gastric juices containing hydrochloric acid and digestive enzymes like pepsin, which break down proteins into smaller peptides. The stomach's muscular walls churn and mix food with these digestive secretions, turning it into a semi-liquid substance called chyme. Additionally, the stomach serves as a temporary storage site for food, releasing it gradually into the small intestine for further digestion. It also plays a role in absorbing certain substances, such as alcohol and some medications, and acts as a barrier against harmful pathogens through its acidic environment.",
        "system": "DigestiveSystem"
    },
    {
        "name": "Small_Intestine",
        "latin": "intestinum tenue",
        "mainFunction": "The small intestine is a crucial organ in the digestive system, primarily responsible for the absorption of nutrients and minerals from food. It is divided into three sections: the duodenum, jejunum, and ileum. In the duodenum, digestive enzymes and bile mix with chyme to break down carbohydrates, proteins, and fats into simpler molecules. The jejunum and ileum are specialized for the absorption of these nutrients into the bloodstream through their highly folded inner walls lined with villi and microvilli, which significantly increase surface area. The small intestine also plays a role in water absorption and immune function by hosting gut-associated lymphoid tissue (GALT), which helps protect the body from pathogens.",
        "system": "DigestiveSystem"
    },
    {
        "name": "Liver",
        "latin": "hepar",
        "mainFunction": "The liver is a vital organ with multiple essential functions, primarily related to metabolism, detoxification, and digestion. It produces bile, which helps in the emulsification and breakdown of fats during digestion. The liver also processes nutrients absorbed from the small intestine, converting them into energy or storing them as glycogen for future use. Additionally, it detoxifies harmful substances, including alcohol, drugs, and metabolic byproducts, ensuring they are safely eliminated from the body. The liver synthesizes important proteins such as albumin and clotting factors, regulates blood sugar levels, and stores vitamins and minerals like iron. It plays a critical role in maintaining overall homeostasis and metabolic balance.",
        "system": "DigestiveSystem"
    },
    {
        "name": "Brain",
        "latin": "cerebrum",
        "mainFunction": "The brain is the control center of the body, responsible for regulating and coordinating all physiological and cognitive functions. It processes sensory information, such as sight, sound, touch, taste, and smell, enabling perception and interaction with the environment. The brain controls voluntary movements, regulates vital involuntary functions like heartbeat and breathing, and maintains homeostasis. It is also the seat of higher cognitive functions, including thinking, memory, learning, emotions, and decision-making. Divided into specialized regions such as the cerebrum, cerebellum, and brainstem, the brain orchestrates complex activities, ensuring the body's survival, adaptation, and functioning in a constantly changing environment.",
        "system": "NervousSystem"
    },
    {
        "name": "Spinal_Cord",
        "latin": "medulla spinalis",
        "mainFunction": "The spinal cord is a vital part of the central nervous system that serves as the communication highway between the brain and the rest of the body. It transmits sensory information from the body to the brain and motor commands from the brain to the muscles, enabling movement and sensation. Protected by the vertebral column, the spinal cord also houses reflex arcs, allowing for immediate, involuntary responses to certain stimuli without involving the brain, such as withdrawing a hand from a hot surface. Additionally, it plays a role in regulating autonomic functions and ensuring the coordination of complex motor activities, making it essential for both voluntary and involuntary actions.",
        "system": "NervousSystem"
    },
    {
        "name": "Nerves",
        "latin": "nervi",
        "mainFunction": "Nerves are integral components of the peripheral nervous system, responsible for transmitting electrical signals between the brain, spinal cord, and the rest of the body. They carry sensory information from the body's tissues and organs to the central nervous system (CNS) and deliver motor commands from the CNS to muscles, enabling movement and responses. Nerves are composed of bundles of axons surrounded by protective layers, which ensure efficient and precise signal transmission. They are classified into three main types: sensory nerves (carrying sensory input), motor nerves (controlling movement), and mixed nerves (handling both sensory and motor functions). Nerves play a critical role in sensation, motor control, and the regulation of autonomic functions like heart rate and digestion.",
        "system": "NervousSystem"
    },
    {
        "name": "Biceps",
        "latin": "biceps brachii",
        "mainFunction": "The biceps, formally known as the biceps brachii, is a large, two-headed muscle located in the upper arm between the shoulder and the elbow. Its primary function is to facilitate the movement of the forearm and elbow joint by enabling flexion (bending the elbow) and supination (rotating the forearm so the palm faces upward). The biceps also assist in stabilizing the shoulder joint during various activities. This muscle is essential for many everyday movements, such as lifting, pulling, and carrying objects, and it plays a critical role in upper body strength and coordination.",
        "system": "MuscularSystem"
    },
    {
        "name": "Quadriceps",
        "latin": "quadriceps femoris",
        "mainFunction": "The quadriceps, commonly referred to as the quads, are a group of four muscles located at the front of the thigh. These muscles include the rectus femoris, vastus lateralis, vastus medialis, and vastus intermedius. The primary function of the quadriceps is to extend the knee joint, which is essential for movements like walking, running, jumping, and climbing. The rectus femoris also assists in hip flexion, making the quadriceps crucial for activities that require leg strength and mobility. Additionally, the quadriceps play a key role in stabilizing the knee joint and maintaining balance during weight-bearing activities.",
        "system": "MuscularSystem"
    },
    {
        "name": "Pectoral_Muscles",
        "latin": "musculus pectoralis",
        "mainFunction": "The pectoral muscles, commonly known as the 'pecs,' are a group of muscles located in the chest that play a crucial role in upper body movement. The primary muscles are the **pectoralis major** and **pectoralis minor**. The pectoralis major is responsible for movements such as flexion, adduction, and internal rotation of the shoulder joint, allowing actions like pushing, lifting, and bringing the arms across the body. The pectoralis minor lies beneath the major and aids in stabilizing the shoulder blade (scapula) and assisting in movements like downward rotation and depression of the scapula. Together, these muscles provide strength, mobility, and support for various upper body activities, including pushing and lifting motions.",
        "system": "MuscularSystem"
    },
    {
        "name": "Skull",
        "latin": "cranium",
        "mainFunction": "The skull is a bony structure that serves as the protective framework for the brain and the sensory organs. Comprising 22 bones, it is divided into two main parts: the **cranium**, which encases and safeguards the brain, and the **facial bones**, which provide structure and support for the face, including the eyes, nose, and mouth. The skull also houses and protects delicate structures like the inner ear and sinuses, and it serves as an attachment point for muscles involved in chewing, facial expression, and head movement. Its role is essential in providing physical protection to the brain and sensory organs while enabling vital functions like eating, breathing, and communication.",
        "system": "SkeletalSystem"
    },
    {
        "name": "Femur",
        "latin": "femur",
        "mainFunction": "The femur, commonly known as the thigh bone, is the longest, strongest, and heaviest bone in the human body. Located in the upper leg, it serves as a critical component of the skeletal system, supporting the body's weight during standing, walking, running, and jumping. The femur connects the hip joint to the knee joint, enabling a wide range of motion, including flexion, extension, and rotation. Its proximal end articulates with the pelvis at the hip joint, forming a ball-and-socket structure that allows mobility, while its distal end connects to the tibia and patella at the knee joint. The femur also acts as a site for muscle attachment, facilitating movement and maintaining stability in the lower limb.",
        "system": "SkeletalSystem"
    },
    {
        "name": "Rib_Cage",
        "latin": "costa",
        "mainFunction": "The rib cage is a bony and cartilaginous structure that surrounds and protects the vital organs within the thoracic cavity, including the heart and lungs. Comprising 12 pairs of ribs, the sternum (breastbone), and the thoracic vertebrae, the rib cage plays a crucial role in supporting respiration by expanding and contracting during breathing, allowing the lungs to fill with and expel air. It also provides attachment points for muscles involved in breathing, posture, and upper body movement. Beyond its protective function, the rib cage contributes to the overall structural integrity of the upper body, maintaining stability and flexibility for daily activities.",
        "system": "SkeletalSystem"
    },
    {
        "name": "Thyroid",
        "latin": "glandula thyreoidea",
        "mainFunction": "The thyroid is a butterfly-shaped gland located in the front of the neck, just below the Adam's apple. It plays a crucial role in regulating the body's metabolism through the production of hormones, primarily thyroxine (T4) and triiodothyronine (T3). These hormones influence various bodily functions, including energy production, temperature regulation, heart rate, and the metabolism of fats, proteins, and carbohydrates. The thyroid gland is also involved in growth and development, particularly in children. Additionally, it works closely with the pituitary gland and hypothalamus to maintain hormonal balance through a feedback system. Proper thyroid function is essential for overall health and well-being.",
        "system": "EndocrineSystem"
    },
    {
        "name": "Pancreas",
        "latin": "pancreas",
        "mainFunction": "The pancreas is a vital organ located in the abdomen, behind the stomach, with both endocrine and exocrine functions. Its primary endocrine role is to regulate blood sugar levels by producing hormones such as insulin, which lowers blood sugar, and glucagon, which raises it. The pancreas also secretes somatostatin, which helps regulate other hormones. On the exocrine side, it produces digestive enzymes, including amylase, lipase, and proteases, which are released into the small intestine to help break down carbohydrates, fats, and proteins. By combining these functions, the pancreas plays a crucial role in maintaining metabolic balance and ensuring efficient digestion and nutrient absorption.",
        "system": "EndocrineSystem"
    },
    {
        "name": "Adrenal_Glands",
        "latin": "glandulae suprarenales",
        "mainFunction": "The adrenal glands are small, triangular-shaped endocrine glands located on top of each kidney. They play a vital role in regulating various physiological processes through the production of hormones. The adrenal glands consist of two main parts: the **cortex** and the **medulla**, each with distinct functions. The cortex produces hormones such as cortisol, which helps regulate metabolism, stress response, and immune function, and aldosterone, which controls blood pressure and electrolyte balance. The medulla produces catecholamines, including adrenaline and noradrenaline, which prepare the body for 'fight or flight' responses by increasing heart rate, blood pressure, and energy availability. Together, these hormones help maintain homeostasis and enable the body to adapt to stress and changing environmental conditions.",
        "system": "EndocrineSystem"
    },
    {
        "name": "Lymph_Nodes",
        "latin": "noduli lymphatici",
        "mainFunction": "Lymph nodes are small, bean-shaped structures that are an integral part of the lymphatic system. They play a crucial role in the immune system by filtering lymph, a fluid that contains waste products, pathogens, and immune cells. Lymph nodes are strategically located throughout the body, often in clusters in areas like the neck, armpits, groin, and abdomen. Their primary function is to trap and destroy harmful substances, such as bacteria, viruses, and cancer cells, using specialized immune cells like lymphocytes and macrophages. By filtering lymph and facilitating the activation of immune responses, lymph nodes help protect the body from infections and maintain overall immune health.",
        "system": "LymphaticSystem"
    },
    {
        "name": "Spleen",
        "latin": "splen",
        "mainFunction": "The spleen is an important organ located in the upper left abdomen, just beneath the rib cage. Its primary functions are related to the immune system and blood filtration. It filters the blood by removing old or damaged red blood cells and recycling their components, such as iron, for reuse. The spleen also plays a key role in the immune response by detecting and fighting infections; it produces and stores white blood cells, particularly lymphocytes, which help combat pathogens. Additionally, the spleen acts as a reservoir for blood, releasing it into the circulatory system during times of high demand, such as physical exertion or blood loss. This multifunctional organ is essential for maintaining both immune defense and blood health.",
        "system": "LymphaticSystem"
    },
    {
        "name": "Thymus",
        "latin": "thymus",
        "mainFunction": "The thymus is a small, specialized organ located in the upper chest, just behind the sternum and between the lungs. It plays a crucial role in the development and function of the immune system, particularly during early life and adolescence. The thymus is responsible for the maturation of T-lymphocytes (T-cells), a type of white blood cell that is essential for adaptive immunity. These T-cells help the body recognize and combat pathogens, as well as detect and destroy abnormal cells, such as those that are cancerous. The thymus is most active during childhood and gradually shrinks with age, a process known as involution. Despite its reduced size in adulthood, it leaves a lasting impact on the immune system by producing a diverse and functional repertoire of T-cells during earlier stages of life.",
        "system": "LymphaticSystem"
    },
    {
        "name": "Kidneys",
        "latin": "renes",
        "mainFunction": "The kidneys are two bean-shaped organs located on either side of the spine, just below the ribcage. Their primary function is to filter and remove waste products, toxins, and excess water from the blood, forming urine, which is excreted through the urinary system. Additionally, the kidneys regulate important bodily functions such as maintaining fluid and electrolyte balance, controlling blood pressure by managing blood volume and releasing hormones like renin, and producing erythropoietin, which stimulates red blood cell production in the bone marrow. The kidneys also help maintain the body’s acid-base balance, ensuring proper pH levels for cellular function. These essential organs play a critical role in homeostasis and overall metabolic health.",
        "system": "UrinarySystem"
    },
    {
        "name": "Bladder",
        "latin": "vesica urinaria",
        "mainFunction": "The bladder is a hollow, muscular organ located in the pelvis that serves as the storage site for urine before it is excreted from the body. It collects urine produced by the kidneys through two tubes called ureters and temporarily holds it until voluntary urination occurs. The bladder can expand and contract due to its elastic walls and muscular layers, allowing it to store varying amounts of urine. Its function is controlled by a combination of voluntary and involuntary muscle actions, including the detrusor muscle for contraction and sphincters to regulate the release of urine. The bladder plays a critical role in the urinary system, helping maintain fluid and waste balance in the body.",
        "system": "UrinarySystem"
    },
    {
        "name": "Urethra",
        "latin": "urethra",
        "mainFunction": "The urethra is a tubular structure that serves as the final passageway for urine to exit the body from the bladder. In males, the urethra is longer and also functions as a conduit for semen during ejaculation, as it passes through the prostate gland and penis. In females, the urethra is shorter and serves only for urinary excretion, opening just above the vaginal opening. The urethra is surrounded by muscles, including the external urethral sphincter, which allows for voluntary control of urination. Its primary function is to facilitate the removal of urine from the body while maintaining control over the timing and flow.",
        "system": "UrinarySystem"
    },
    {
        "name": "Testes",
        "latin": "testes",
        "mainFunction": "The testes, also known as testicles, are oval-shaped organs located in the scrotum, outside the male body. Their primary functions are the production of sperm, necessary for reproduction, and the secretion of testosterone, the primary male sex hormone. Testosterone plays a critical role in the development of male secondary sexual characteristics, such as increased muscle mass, body hair growth, and a deeper voice, as well as the regulation of libido and fertility. The testes are divided into numerous seminiferous tubules, where sperm cells are produced and begin their maturation process. By fulfilling these reproductive and hormonal roles, the testes are essential for male reproductive health and overall endocrine function.",
        "system": "MaleReproductiveSystem"
    },
    {
        "name": "Ovaries",
        "latin": "ova",
        "mainFunction": "The ovaries are a pair of almond-shaped organs located on either side of the uterus in the female reproductive system. Their primary functions are to produce and release eggs (ova) for reproduction and to secrete the hormones estrogen and progesterone, which regulate the menstrual cycle, ovulation, and pregnancy. Each month during the reproductive years, one ovary releases a mature egg in a process called ovulation. The ovaries also play a vital role in the development of female secondary sexual characteristics, such as breast development and the regulation of body fat distribution. Additionally, the hormones produced by the ovaries help maintain bone density, cardiovascular health, and overall reproductive health.",
        "system": "FemaleReproductiveSystem"
    },
    {
        "name": "Uterus",
        "latin": "uterus",
        "mainFunction": "The uterus, commonly known as the womb, is a hollow, muscular organ located in the female pelvis, between the bladder and rectum. Its primary function is to nurture and support a fertilized egg during pregnancy. Once an egg is fertilized, it implants in the thick, nutrient-rich lining of the uterus, called the endometrium, where it develops into an embryo and eventually a fetus. The uterus also plays a critical role during childbirth, with its strong muscular walls contracting to help deliver the baby. In non-pregnant cycles, the uterus sheds its lining during menstruation if no fertilization occurs. It is a central organ in the female reproductive system, essential for fertility, pregnancy, and childbirth.",
        "system": "FemaleReproductiveSystem"
    },
    {
        "name": "Skin",
        "latin": "cutis",
        "mainFunction": "The skin is the largest organ of the human body, serving as a protective barrier between the internal body and the external environment. Its primary function is to shield the body from harmful elements, such as pathogens, UV radiation, and physical injuries. The skin also plays a crucial role in regulating body temperature through sweating and blood vessel dilation or constriction. It is involved in sensory perception, allowing the detection of touch, pressure, temperature, and pain. Additionally, the skin synthesizes vitamin D when exposed to sunlight, which is essential for bone health. Composed of three main layers—the epidermis, dermis, and hypodermis—the skin also helps retain moisture, prevents dehydration, and contributes to immune defense, making it vital for overall health and homeostasis.",
        "system": "IntegumentarySystem"
    },
    {
        "name": "Hair",
        "latin": "capilli",
        "mainFunction": "Hair serves multiple functions in humans, primarily providing protection, sensory input, and temperature regulation. On the scalp, hair protects the skin from ultraviolet (UV) radiation and insulates against heat loss. Eyelashes and eyebrows help shield the eyes from dust, sweat, and other particles, while nasal and ear hair prevent debris from entering the respiratory and auditory systems. Hair also enhances sensory perception by detecting subtle movements or changes in the environment through its connection to nerve endings in the skin. Additionally, hair plays a role in social and cultural expression, contributing to identity and aesthetics. Its growth and health reflect overall well-being and are influenced by genetics, hormones, and nutrition.",
        "system": "IntegumentarySystem"
    },
    {
        "name": "Nails",
        "latin": "ungues",
        "mainFunction": "Nails are hard, protective coverings made of keratin, located at the tips of fingers and toes. Their primary function is to protect the sensitive tissues beneath them from injury and external damage. Nails also enhance fine motor skills by providing support and precision for tasks like gripping, picking, or scratching. Additionally, they play a role in sensory perception by amplifying the sense of touch through the pressure they exert on the fingertips. Nails are also indicators of overall health, as changes in their color, texture, or growth can signal underlying medical conditions. Their growth and maintenance reflect proper nutrition and hygiene.",
        "system": "IntegumentarySystem"
    }
]


    # Create instances for systems
    systems_instances = {}
    for system in systems_data:
        system_instance = System(system["name"])
        system_instance.label = system["label"]
        system_instance.description = system["description"]
        systems_instances[system["name"]] = system_instance

    # Create instances for organs and link them to systems
    for organ in organs_data:
        organ_instance = Organs(organ["name"])
        organ_instance.latin = organ["latin"]
        organ_instance.mainFunction = organ["mainFunction"]
        # Link the organ to its system using the system name
        organ_instance.isPartOf.append(systems_instances[organ["system"]])

    # Save the ontology to a file
    onto.save(file=FILE_NAME, format="rdfxml")

# Print out organ and system details
print("Organs:")
for organ in onto.Organs.instances():
    print(f"  {organ.name}: Latin = {organ.latin}, Main Function = {organ.mainFunction}, Part of = {organ.isPartOf[0].label}")

print("\nSystems:")
for system in onto.System.instances():
    print(f"  {system.name}: Label = {system.label}, Description = {system.description}")
