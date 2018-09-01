from IPython.display import display, HTML

def list_numbered(keyword):
    pass

def codehider():
    """
    Adds a code hider button to the current cell output.
    """
    return display(HTML('''
        <script>
        function code_toggle() {
         var buttons = document.querySelectorAll('[id^="CodeButton_"]');
         if ($("div.input").is(':visible')){
             $("div.input").hide('500');
             for (var i = 0; i < buttons.length; i++) {
                 $(buttons[i]).val('Show code cells.');
             }
         } else {
             $("div.input").show('500');
             for (var i = 0; i < buttons.length; i++) {
                 $(buttons[i]).val('Hide code cells.');
             }
         }
        }

        $( document ).ready(function(){ $('div.input').hide() });
        </script>

        <form action="javascript:code_toggle()"><input type="submit" id="CodeButton_inline" value="Show code cells"></form>
        '''))

# einmalig parallel zu dem anderen ToC managen -> zwei unabhängige ToC
def tableofcontent(maxlevel=3, updatefrequency=300000, exclude_ids=[]):
    """
    Adds a floating code hider button and table of content to the top right of
    the notebook. Only the first apperance of equal headlines is linked. This
    can also be used to add a table of content somewhere in a markdown cell.

    To add a table of content in a markdown cell use the following code:
        <h2 id="tocheading">Table of Content</h2>
        <div id="tocinline"></div>

    maxlevel: Set the max level to which headlines are added.
    """
    options = {'maxlevel': maxlevel,
               'updatefrequency': updatefrequency,
               'exclude': '['+','.join(['"'+e+'"' for e in exclude_ids])+']'}
    return display(HTML('''<script>
// Converts integer to roman numeral
function romanize(num) {
    var lookup = {M:1000,CM:900,D:500,CD:400,C:100,XC:90,L:50,XL:40,X:10,IX:9,V:5,IV:4,I:1},
        roman = '',
        i;
    for ( i in lookup ) {
        while ( num >= lookup[i] ) {
        roman += i;
        num -= lookup[i];
        }
    }
    return roman;
}

// Builds a <ul> Table of Contents from all <headers> in DOM
function createTOC(toc_tag, maxlevel){
    var toc = "";
    var level = 0;
    var levels = {};
    $('#'+toc_tag).html('');

    $(":header").each(function(i){
        if (this.id=='tocheading'){return;}
        if (this.tagName[1] >= maxlevel){return;}

        var titleText = this.innerHTML;
        var openLevel = this.tagName[1];

        var exclude = %(exclude)s;
        for (var i = 0; i < exclude.length; i++) {
            if (titleText.indexOf(exclude[i]) !== -1){return;}
        }

        if (levels[openLevel]){
        levels[openLevel] += 1;
        } else{
        levels[openLevel] = 1;
        }

        if (openLevel > level) {
        toc += (new Array(openLevel - level + 1)).join('<ul class="'+toc_tag+'">');
        } else if (openLevel < level) {
        toc += (new Array(level - openLevel + 1)).join("</ul>");
        for (i=level;i>openLevel;i--){levels[i]=0;}
        }

        level = parseInt(openLevel);

        if (this.id==''){this.id = this.innerHTML.replace(/ /g,"-")}
        var anchor = this.id;

        toc += '<li><a href="#' + escape(anchor) + '">'
        + romanize(levels[openLevel].toString()) + '. ' + titleText
        + '</a></li>';

    });

    if (level) {
    toc += (new Array(level + 1)).join("</ul>");
    }

    $('#'+toc_tag).append(toc);
};

// Executes the createTOC_inline function
setTimeout(function(){createTOC('tocinline', 1 + %(maxlevel)s);},1000);
setTimeout(function(){createTOC('tocinline', 1 + %(maxlevel)s);},5000);
setTimeout(function(){createTOC('tocinline', 1 + %(maxlevel)s);},15000);

// Rebuild TOC_inline every 5 minutes
setInterval(function(){createTOC('tocinline', 1 + %(maxlevel)s);}, %(updatefrequency)s);

</script>

<h2 id="tocheading">Table of Content</h2>
<div id="tocinline"></div>

''' % options))
