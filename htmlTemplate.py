css = '''
<style>
.chat-message {
   padding: 1.5rem;
   border-radius: 0.5rem;
   margin-bottom: 1rem;
   display: flex
   }
   .chat-message.user{
       background-color: #e0f7fa
    }
    .chat-message.bot{
        background-color: #fce4ec
    }
    .chat-message .avatar {
        width: 15%;
        height: 15%;
    }
    .chat-message .avatar img {
         max-width: 78px;
         max-height: 78px;
         border-radius: 50%;
         object-fit: cover;
        
    }
    .chat-message .message {
        width: 85%;
        padding: 0 1.5rem;
        color: #333;
    }
    '''
    
    
bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
      <img src="c:/Users/iquba/Downloads/125887871_Graident Ai Robot.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
      <img src="c:/Users/iquba/Downloads/hector-reyes-PXjQaGxi4JA-unsplash.jpg">
      </div>
      <div class="message">{{MSG}}</div>
</div>
'''

