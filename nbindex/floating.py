from IPython.display import display, HTML

# Example:
#  from nbindex import utils, floating
#  utils.combine(floating.tableofcontent(),
#                floating.codehider())

def attribution(html_string):
    return display(HTML('''
        <script>
        $('<div id="attribution_footer" style="float:right; color:#999; background:#fff;"> </div>').css({position: 'fixed', bottom: '0px', right: 20}).appendTo(document.body);
        $('#attribution_footer').html('%s');
        </script>
        '''))

def codehider(position={'top': '110px', 'right': '20px'}):
    """
    Adds a floating code hider button to the top right of the notebook.
    """
    return display(HTML('''
        <script>
        function code_toggle() {
         if ($("div.input").is(':visible')){
             $("div.input").hide('500');
             $('#CodeButton').val('Show all Code');
             $('#CodeButton_inline').val('Show all code in this notebook');
         } else {
             $("div.input").show('500');
             $('#CodeButton').val('Hide all Code');
             $('#CodeButton_inline').val('Hide all code in this notebook');
         }
        }

        $( document ).ready(function(){ $('div.input').hide() });

        if (!($('#CodeButton').length)) {
            $('<form action="javascript:code_toggle()" id="CodeButtonForm"><input type="submit" id="CodeButton" value="Show all code"></form>').css({position: 'fixed', top: "%(top)s", right: "%(right)s", background: "rgba(255, 255, 255, 0.6)"}).appendTo(document.body);
        } else {
            document.getElementById('CodeButtonForm').style.top = "%(top)s";
            document.getElementById('CodeButtonForm').style.right = "%(right)s";
            $('#CodeButton').val('Show all Code');
        }

        </script>

        <form action="javascript:code_toggle()"><input type="submit" id="CodeButton_inline" value="Show all code in this notebook"></form>
        ''' % position))

def tableofcontent(maxlevel=3, position={'top': '135px', 'right': '20px'}):
    """
    Adds a floating code hider button and table of content to the top right of
    the notebook. Only the first apperance of equal headlines is linked. This
    can also be used to add a table of content somewhere in a markdown cell.

    To add a table of content in a markdown cell use the following code:
        <h2 id="tocheading">Table of Content</h2>
        <div id="tocinline"></div>

    maxlevel: Set the max level to which headlines are added.
    """
    position.update({'maxlevel': maxlevel})
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

////////////////////////////////////////////////////////////////////////////////

// Builds a <ul> Table of Contents from all <headers> in DOM
function createTOC(toc_tag){
    var toc = "";
    var level = 0;
    var maxlevel = 1 + %(maxlevel)s;
    var levels = {};
    $('#'+toc_tag).html('');

    $(":header").each(function(i){
        if (this.id=='tocheading'){return;}
        if (this.tagName[1] >= maxlevel){return;}

        var titleText = this.innerHTML;
        var openLevel = this.tagName[1];

        // Wiki hacks
        if (titleText.indexOf("User Tools") !== -1){return;}
        if (titleText.indexOf("Site Tools") !== -1){return;}
        if (titleText.indexOf("Page Tools") !== -1){return;}
        if (titleText.indexOf("XENON1TWiki") !== -1){return;}

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

////////////////////////////////////////////////////////////////////////////////

// Executes the createTOC_inline function
setTimeout(function(){createTOC('tocinline');},1000);
setTimeout(function(){createTOC('tocinline');},5000);
setTimeout(function(){createTOC('tocinline');},15000);

// Rebuild TOC_inline every 5 minutes
setInterval(function(){createTOC('tocinline');},300000);

////////////////////////////////////////////////////////////////////////////////

$('<div id="toc"></div>').css({position: 'fixed', top: '160px', right: 20, background: "rgba(255, 255, 255, 0.6)"}).appendTo(document.body);
$("#toc").css("z-index", "2000");

// Executes the createToc function
setTimeout(function(){createTOC('toc');},100);
setTimeout(function(){createTOC('toc');},5000);
setTimeout(function(){createTOC('toc');},15000);

// Rebuild TOC every 5 minutes
setInterval(function(){createTOC('toc');},300000);

////////////////////////////////////////////////////////////////////////////////

function toc_toggle() {
 if ($('#toc').is(':visible')){
     $('#toc').hide('500');
     $('#tocButton').val('Show table of content')
 } else {
     $('#toc').show('500');
     $('#tocButton').val('Hide table of content')
 }
}

if (!($('#tocButton').length)) {
    $('<form action="javascript:toc_toggle()" id="tocButtonForm"><input type="submit" id="tocButton" value="Hide table of content"></form>').css({position: 'fixed', top: "%(top)s", right: "%(right)s", background: "rgba(255, 255, 255, 0.6)"}).appendTo(document.body);
} else {
    document.getElementById('tocButtonForm').style.top = "%(top)s";
    document.getElementById('tocButtonForm').style.right = "%(right)s";
    $('#tocButton').val('Hide table of content')
}

////////////////////////////////////////////////////////////////////////////////

</script>
''' % position))
