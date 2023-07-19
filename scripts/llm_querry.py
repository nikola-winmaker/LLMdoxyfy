import openai
import certifi
certifi.where()

# Set your OpenAI API key



# Define a function to interact with the chat model
def LlmDoxify(function_code):

    user_input = "Write a doxygen comment for this C function:\n" + function_code + \
                "Always include @brief and detailed description, @param and  @return. "
    response = openai.Completion.create(
        engine='text-davinci-003',  # Specify the engine
        prompt= 'User: ' + user_input + '\nAssistant:',
        max_tokens=200,  # Adjust as needed
        temperature=0.7,  # Controls randomness of the output, lower values make it more focused
        n=1,  # Specify the number of responses to generate
        stop=None  # Specify a stop sequence to end the response early (optional)
    )

    answer = response.choices[0].text.strip()
    return answer


if __name__ == "__main__":
    # Example usage
    # while True:
    #     user_input = input('User: ')
    #     if user_input.lower() == 'exit':
    #         break

    fnc_code = """
    void keypad_read_cb(lv_indev_drv_t * drv, lv_indev_data_t *data) {
    // Read the button matrix state and set the data accordingly
    button_function_t button_function = read_bmatrix_key();
    lv_obj_t *object_to_focus = NULL;




    data->state = LV_INDEV_STATE_REL;

    switch(screen_state){
        case HOME_SCREEN:
            object_to_focus = home_scr_navigation(button_function);
        break;
        default:
            return;
        break;
    }

    if (button_function != BUTTON_UNKNOWN) {
        if (button_function == BUTTON_START_OK) {
            data->key = LV_KEY_ENTER;
            data->state = LV_INDEV_STATE_PR;
            ESP_LOGI(TAG, "BUTTON_START_OK");

        } else if (button_function == BUTTON_STOP_BACK) {
            data->key = LV_KEY_ESC;
            data->state = LV_INDEV_STATE_PR;
            ESP_LOGI(TAG, "BUTTON_STOP_BACK");
        }
        // reset button_function
        clear_bmatrix_key();

        //LV_INDEV_STATE_REL
        lv_group_focus_obj(object_to_focus);
    }
    """


    response = LlmDoxify(fnc_code)
    print('Assistant:', response)

