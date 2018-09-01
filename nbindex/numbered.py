from IPython.display import display, HTML

def object(keyword, description=""):
    """
    Adds numbered named object HTML anchors. Link to them in MarkDown using: [to keyword 1](#keyword-1)
    """
    return display(HTML('''<div id="%s"></div> %s
    <script>
    var fignb = 1;
    var key = "%s"
    $("div").each(function(i){
        if (this.id === key){
            this.innerHTML = '<a name="' + key + '-' + fignb.toString() + '"></a>' +
                             '<a class="anchor" href="#' + key + '-' + fignb.toString() +'"><b><i>' + key.charAt(0).toUpperCase() + key.slice(1) + ' ' + fignb.toString() + '</i></b></a>';
            fignb += 1;
        }
    });
    </script>
    ''' % (keyword,description,keyword)))

def Figure(description=""):
    """
    Adds numbered Figure HTML anchors. Link to them in MarkDown using: [to Figure 1](#Figure-1)
    """
    return object("Figure", description)

def Table(description=""):
    """
    Adds numbered Table HTML anchors. Link to them in MarkDown using: [to Table 1](#Table-1)
    """
    return object("Table", description)

def Image(description=""):
    """
    Adds numbered Image HTML anchors. Link to them in MarkDown using: [to Image 1](#Image-1)
    """
    return object("Image", description)
