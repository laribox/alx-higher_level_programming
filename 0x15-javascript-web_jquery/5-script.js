const htmlDoc = $(document);
const item = '<li>Item</li>';
const ulClass = $('UL.my_list');
const addItemDiv = $('DIV#add_item');
const addAnItem = () => ulClass.append(item);

htmlDoc.ready(addItemDiv.on('click', addAnItem));
