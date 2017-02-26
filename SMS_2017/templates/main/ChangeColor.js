
function changeColor(value)
{
    var color = document.body.style.backgroundColor;
    switch(value)
    {
        case 'r':
            color = "#FF0000";
        break;
        case 'g':
            color = "#0000FF";
        break;
        break;
    }
    document.body.style.backgroundColor = color;
}