from datetime import datetime 

class Post:

    def __init__(self, user_id, title, text, post_datetime=datetime.now()):

        validation_errors = []

        if not user_id:

            validation_errors.append('User ID must be provided')

        title = title.strip() 

        if not title:  # None and empty strings are False 
            validation_errors.append('Title must be provided and not blank')

        text = text.strip()

        if not text: 
            validation_errors.append('Text must be provided and not blank ')
        
        now = datetime.now()

        if post_datetime > now:  # is the date in the future? number of seconds greater than the current number of seconds 
            validation_errors.append('Timestamp must be now or in the past')

        if validation_errors:
            raise ValueError(*validation_errors)

        self.user_id = user_id
        self.title = title
        self.text = text 
        self.post_datetime = post_datetime