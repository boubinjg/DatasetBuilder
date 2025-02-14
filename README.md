# DatasetBuilder
An application that randomly samples input images for subimages that can be used for 
training machine learning algorithms.

Dependencies:
    Pillow
    Tkinter
    Python2/3

DataserBuilder.py Arguments:
    Arg 1: Sample image being split
        Each participant's images can be found in $Participant/Samples
        Provide the relative path to the image to the application as arg 1.
    Arg 2: Participants Classification Directory (E.g Jayson, Trey, etc)
        Basically, just provide your first name as the second argument
        This allows the application to know where you store your classified images
    Arg 3: Session # (eg 1, 2 ...)
        Session# is used to differentiate subimages from different training sessions.
        Provide an integer (1-20) identifying your current session.
        Each image should be split 250 times over 1 session.

Usage:
    using this application is simple. Simply execute the script with
    the above arguments. If the subimage you see contains corn, click D 
    on your keyboard. If the image does not contain primarily corn, click F.
    
    When you click D or F, the subimage will be placed in either the directory
    PWD/$Participant/yes or PWD/$Participant/no
    Yes if you click D, No if you click F.

    The image will have a name that includes your session #, name, and classification.

    Each participant's /samples/ directory contains 20 4k images of corn at
    various stages of the growth cycle. For each of these images, you should
    run one session of DatasetBuilder with a unique session number provided.

    Each session of DatasetBuilder lasts for 250 iterations. You will see 250 
    different random subimages of the corn field image, and must classify them.
    Once the 250th subimage is classified, the session ends and the application closes.
    
    If, in the middle of training, you misclassify a sample by accident, you can
    easily find it in your yes/no directories by its sesion ID and session count (which is on the GUI).
    Just go into the yes/no directory and move it.

Please let me know if you have any questions
-JB

