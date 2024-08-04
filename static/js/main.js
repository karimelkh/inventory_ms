/*
 * TODO: enhance code
 * this code needs more enhancements amd fixes
 * */
$(document).ready(function () {
	$("#tog-usermenu").click(toggleUserMenu);
	$("#tog-newmenu").click(toggleNewMenu);
	$("#tog-browsemenu").click(toggleBrowseMenu);
	$("#tog-colsmenu").click(toggleColsMenu);
	$("input[name='col']").on("change", updateTable);
	$("#to_cpy").click(copyToClip);
	// $("#rm-item").click(removeItemPopUp);
	$("#ud-item").click(updateItemPopUp);
	$("#item-img").click(zoomInImg);
	$("#modal-img > img").click(zoomOutImg);
	$("#overlay, #img-modal, #modal-img > img").click(zoomOutImg);
	$("#overlay, form.rm-form button").click(hideRemoveForm);
	// $("#overlay, form.ud-form button").click(hideUpdateForm);
	$("input#select-all").on("change", ToggleRows);
	$("button#del-btn").click(delRows);
	//$("button.update-btn").click(UpdateRow);
});

// use Ajax instead
function delRows() {
	const inputs = $("input[type='checkbox'][name='row']:checked");
	const rmlist = $("form.rm-form div#send-ids");
	inputs.each(function () {
		const id = $(this).data("id");
		const name = $(this).data("name");
		const div = $("<div>");
		const checkbox = $("<input>", {
			type: "checkbox",
			checked: true,
			id: `rm-id-${id}`,
			name: "rm-id",
			value: id,
			class: "mr-3",
		});
		const label = $("<label>", {
			for: `rm-id-${id}`,
			class: "",
			text: `article #${id}: ${name}`,
		});
		div.append(checkbox);
		div.append(label);
		rmlist.append(div);
	});
	removeItemPopUp();
}

function ToggleRows() {
	const selAll = $(this);
	const inputs = $("input[type='checkbox'][name='row']");
	if (selAll.prop("checked")) inputs.prop("checked", true);
	else inputs.prop("checked", false);
}

function hideRemoveForm() {
	$("#rm-pop").hide();
}

function hideRemoveForm() {
	$("#ud-pop").hide();
}

function zoomInImg() {
	$("#img-modal").show();
	$("#overlay").show();
}

function zoomOutImg() {
	$("#img-modal").hide();
	$("#overlay").hide();
}

function toggleUserMenu() {
	$("#usermenu").toggle();
}

function toggleNewMenu() {
	$("#newmenu").toggle();
}

function toggleBrowseMenu() {
	$("#browsemenu").toggle();
}

function toggleColsMenu() {
	$("#colsmenu").toggle();
}

function updateTable() {
	$(this).each(updateCol);
}

function updateCol() {
	const td = $(`td#td-${this.value}`);
	const th = $(`th#th-${this.value}`);
	if (this.checked) {
		td.show();
		th.show();
	} else {
		td.hide();
		th.hide();
	}
}

function copyToClip() {
	const txt = $(this).text().trim().slice(1);
	navigator.clipboard.writeText(txt);
}

function removeItemPopUp() {
	$("#rm-pop").show();
	$("#overlay").show();
}

function updateItemPopUp() {
	$("#ud-pop").show();
	$("#overlay").show();
}
