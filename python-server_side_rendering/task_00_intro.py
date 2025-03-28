import os


def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list
    of attendees.

    Args:
        template (str): The template string with placeholders.
        attendees (list): A list of dictionaries, where each dictionary
            represents an attendee.
        
    """
    output_dir = "."

    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees must be a list of dictionaries.")
        return

    # Handle empty inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    #if not os.path.exists(output_dir):
    #    os.makedirs(output_dir)

    for i, attendee in enumerate(attendees):
        try:
            # Replace missing data with "N/A"
            attendee_data = {k: attendee.get(k, "N/A") for k in
                             ["name", "event_title", "event_date",
                              "event_location"]}
            personalized_content = template.format(**attendee_data)
            output_file_path = f"output_{i+1}.txt"
            with open(output_file_path, "w") as f:
                f.write(personalized_content)
            print(f"Generated invitation for {attendee_data.get('name', 'Guest')} at {output_file_path}")
            print(f"Wrote invitation to: {output_file_path}")
        except Exception as e:
            print(f"Error: Could not generate invitation for attendee "
                  f"{i+1}: {e}")


if __name__ == "__main__":
    # Example Usage
    template = """Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team""" + "\n"
    attendees = [
        {"name": "Alice", "event_title": "Birthday Party",
         "event_date": "2025-03-23", "event_location": "Wonderland"},
        {"name": "Bob", "event_title": "Graduation Ceremony",
         "event_date": "2025-04-01"},
        {"name": "Charlie", "event_location": "Grand Ballroom"},
        {"name": "David", "event_title": "Conference"},
    ]

    generate_invitations(template, attendees)
