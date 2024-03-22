import gpt_2_simple as gpt2
import tensorflow as tf

# Download the 124M pre-trained model (if not already downloaded)
model_name = "124M"
gpt2.download_gpt2(model_name=model_name)

# Start a TensorFlow session
sess = gpt2.start_tf_sess()

# Load the pre-trained model
gpt2.load_gpt2(sess, model_name=model_name)


# function to generate the lessons based on the level
def write_content_for_lessons(subject, level):
    prompt = f"create a content for lesson about {subject} for someone level {level} in python"
    gen_text = gpt2.generate(sess, model_name=model_name, prefix=prompt, return_as_list=True)[0]
    print(f'\n======================= Generated Content for {subject}=======================\n**********************beggining of the generated*********************\n{gen_text}\n********************************end of generated**********************************\n')

# function to generate the questions for each lesson 
def generate_three_questions(type_of_question, subject, level):
    prompt = f"generate 3 short {type_of_question} each question just 20 words about {subject} for level {level}"
    gen_text = gpt2.generate(sess, model_name=model_name, prefix=prompt, return_as_list=True)[0]
    print(f'\n======================= Generated {type_of_question} for {subject} =======================\n**********************beggining of the generated*********************\n{gen_text}\n********************************end of generated**********************************\n')
    gpt2.reset_session(sess)
    

write_content_for_lessons('introduction to python', 'beginner')
generate_three_questions('multiple choice questions', 'introduction to python', 'beginner')

