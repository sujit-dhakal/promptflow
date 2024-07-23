# step 1

        go to the newsprompt folder.
        created the generate_headline node. It takes the heading and body of the news and gives a new heading. In the folder generate_heading.jinja2
        For this we created the input news, heading, body in the Inputs

# step 2:

        created the summary node. It takes the body of the news and give a summary. In the folder it is summary.jinja2
        For this we used the same input news and body in the Inputs
# step 3

        created the load_json.py node for heading output.
        For this we created the heading in the Outputs
# step 4

        created the load_json.py node for body ouput.
        For this we created the body in the Outputs

# step 5

        created the load_json_date.py node for the date output.
        For this we created the date in the Outputs

# step 6

        created the load_json_source node for the source output.
        For this we created the source in the Outputs.

# To run the program

        go to the flow.dag.yaml.
        click on visual editor.
        click on batch run right top corner after run all.
        Click on local file and click on the folder where news.jsonl is stored and select the file.
        After selecting the file yaml file will open and click on the run
        after the program execution is finished. follow the output link in the terminal to see the output.jsonl file.
