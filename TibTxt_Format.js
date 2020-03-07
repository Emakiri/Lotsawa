//<script id="Формат тиб текста">
function FN_Tb_Str() {
    var Tib_Strn = document.Input_Tb_Str.Tib_Strn.value;
    //var Tib_Strn=document.getElementById(Tib_Strn1).value;
    var html = Tib_Strn;

    // заголовок и подзаголовки
    var html = html.replace(/([༄༅།\s]+\S+?ལས[།༔])\s+(\S+?་བཞུགས\S*[།༔]*)/gm, '<h1 class="Toc">$1 $2</h1> <br>\n');
    html = html.replace(/(\S+?ནི[།༔])/gm, '<br><br><h4 class="Topic">$1</h4>\n');
    html = html.replace(/(༈)/gm, '<br><br>$1');
    // цитаты и продолжение цитаты
    html = html.replace(/(\S+?ལས[༔།])\s+(.+?[༔།་]*)\s([།](ཞེས|ཅེས).+?[༔།]+)/gm, '<br><div class=\"cite_src\">$1</div> <div class=\"cite\">$2</div> <br>$3<br>\n');
    html = html.replace(/([།](ཞེས|ཅེས).+?དང[༔།༌]*)(<br>\n)*\s*(.+?[༔།་]*)\s([།](ཞེས|ཅེས).+?[༔།]+)/gm, '$1$3<div class="cite">$4</div> <br>$5<br>\n');
    //заключающий помощник - Terminating particles 
    html = html.replace(/((ག་གོ|ང་ངོ[་]*|ད་དོ|ན་ནོ|བ་བོ|མ་མོ|ར་རོ|ལ་ལོ|ས་སོ|ད་ཏོ|འོ)([༔།{1,2}\s\t])+)[།\s]/gm, '$1<br><br>\n');
    //གམ་ ངམ་ དམ་ ནམ་ བམ་ མམ་ འམ་ རམ་ ལམ་ སམ་ ཏམ་ 	question particles			
    //разделительные частицы
    html = html.replace(/(་)(གི|ཀྱི|གྱི|ཡི|གིས|ཀྱིས|གྱིས|ཡིས|སུ|རུ|ཏུ|ན|ལ|དུ|ཏེ|དེ|སྟེ|དང|ཞིང|ཅིང|ཤིང|ཀྱང|ཡང)([་།༔])/gm, '$1<dfn class="cc" title="сс">$2</dfn>$3');
    html = html.replace(/(འི|འིས|འང|འམ)|འང([་།༔])/gm, '<dfn class="cc" title="сс">$1$2</dfn>');

    var element = document.getElementById("Slovar");
    element.parentNode.removeChild(element);
    //отправка результата
    document.getElementById('Result').innerHTML = html;
};

    //console.log("HELLLOOOOO!!");
    //document.getElementById('Send').addEventListener('click', FN_Tb_Str);

    //<form onsubmit="alert('submit!');return false">
    // <input type="text" size="30" value="tib_text">
    // <input type="submit" value="Send" onclick="Complete();">
    //</form>
//</script>