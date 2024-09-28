/*
 * TODO: enhance code
 * this code needs more enhancements amd fixes
 * to optimize and simplify the code experience
 * */
// vars goes here
// let var = "value";

$(document).ready(function () {
	const zoom = mediumZoom($(".zoom").toArray(), {
		margin: 50,
		background: '#000000bf'
	});
	//$("#tog-usermenu").click(toggleUserMenu);
	//$("#tog-newmenu").click(toggleNewMenu);
	//$("#tog-browsemenu").click(toggleBrowseMenu);
	//$("#tog-colsmenu").click(toggleColsMenu);
	$("input[name='col']").on("change", updateTable);
	//$("#to_cpy").click(copyToClip);
	//$("#item-img").click(zoomInImg);
	//$("#modal-img > img").click(zoomOutImg);
	//$("#overlay, #img-modal, #modal-img > img").click(zoomOutImg);
	//$("#overlay, form.rm-form button").click(hideRemoveForm);
	$("input#select-all").on("change", ToggleRows);
	$("button#del-btn").click(delRows);
	$("button#update-btn").click(updateRow);
	$("button#delete-btn").click(DeleteRecord);
});

function showPopUp()
{
	$("#pop-up").show();
	$("#overlay").show();
}

function DeleteRecord()
{
	$.ajax({
		method: "POST",
		url: "",
		contentType: "application/x-www-form-urlencoded",
		data: {
			action: "getDelConfirm",
			//id: id
		},
		success: function(res) {
			console.log("success");
			if (res.form_html) {
				$(".offcanvas-body").html(res.form_html);
			}
        },
		 error: function() { console.log("failure") }
	});
}

function updateRow()
{
	const id = $(this).data("id");
	$.ajax({
		method: "POST",
		url: "",
		contentType: "application/x-www-form-urlencoded",
		data: {
			action: "getUpdateForm",
			id: id
		},
		success: function(res) {
			console.log("success");
			if (res.form_html) {
				$(".offcanvas-body").html(res.form_html);
			}
        },
		 error: function() { console.log("failure") }
	});
}

// use Ajax instead
function delRows() {
	const inputs = $("input[type='checkbox'][name='row']:checked");
	const popup = $("div#pop-up");
	popup.empty();
	const form = $("<form>", {
		id: "rm-form",
		method: "post",
		class: "rm-form"
	});
	const confirmMsg = $("<p>", {
		text: "Are you sure you want to remove the following records:"
	});
	const list = $("<div>", {
		id: "rmlist"
	});
	const submit = $("<button>", {
		type: "submit",
		name: "action",
		value: "remove", // TODO: TO CHANGE LATER
		class: "btn btn-danger mt-2 me-2", // TEMP MARGIN
		text: "yes"
	});
	const abort = $("<button>", {
		id: "abortdel", // TODO: TO MAP ABOVE LATER to cancel the deletion
		type: "button",
		class: "btn btn-primary mt-2", // TEMP MARGIN
		text: "no"
	});
	form.append(list);
	form.append(submit);
	form.append(abort);
	popup.append(confirmMsg);
	popup.append(form);
	inputs.each(function () {
		const id = $(this).data("id");
		const name = $(this).data("name");
		const div = $("<div>", {
			class: "form-check"
		});
		const checkbox = $("<input>", {
			type: "checkbox",
			checked: true,
			id: `rm-id-${id}`,
			name: "rm-id",
			value: id,
			class: "form-check-input",
		});
		const label = $("<label>", {
			for: `rm-id-${id}`,
			class: "form-check-label",
			html: `article <b>${name}</b> (${id})`,
		});
		div.append(checkbox);
		div.append(label);
		list.append(div);
	});
	showPopUp();
}

function ToggleRows() {
	const selAll = $(this);
	const inputs = $("input[type='checkbox'][name='row']");
	if (selAll.prop("checked")) inputs.prop("checked", true);
	else inputs.prop("checked", false);
}

//function hideRemoveForm() {
//	$("#pop-up").hide();
//}

function hideRemoveForm() {
	$("#pop-up").hide();
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

//function copyToClip() {
//	const txt = $(this).text().trim().slice(1);
//	navigator.clipboard.writeText(txt);
//}
