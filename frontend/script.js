document.getElementById("start-test").addEventListener("click", async function () {
    const testContainer = document.getElementById("test-container");
    const testForm = document.getElementById("test-form");
    testForm.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/test/");
        
        if (!response.ok) {
            throw new Error("API dan noto‘g‘ri javob keldi!");
        }

        const savollar = await response.json();
        
        savollar.forEach((savol, index) => {
            const div = document.createElement("div");
            div.innerHTML = `
                <p><strong>${index + 1}. ${savol.matn}</strong></p>
                <input type="radio" name="savol${savol.id}" value="${savol.variant_a}" required> ${savol.variant_a}<br>
                <input type="radio" name="savol${savol.id}" value="${savol.variant_b}"> ${savol.variant_b}<br>
                <input type="radio" name="savol${savol.id}" value="${savol.variant_c}"> ${savol.variant_c}<br>
                <input type="radio" name="savol${savol.id}" value="${savol.variant_d}"> ${savol.variant_d}<br>
            `;
            testForm.appendChild(div);
        });

        testContainer.classList.remove("hidden");
    } catch (error) {
        console.error("Xatolik: ", error);
    }
});

document.getElementById("submit-test").addEventListener("click", async function (event) {
    event.preventDefault();
    
    const ism = document.getElementById("ism").value.trim();
    if (!ism) {
        alert("Ismingizni kiriting!");
        return;
    }

    const formData = new FormData(document.getElementById("test-form"));
    let javoblar = {};

    formData.forEach((value, key) => {
        javoblar[key.replace("savol", "")] = value;
    });

    const response = await fetch("http://127.0.0.1:8000/test/natija", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ism, javoblar })
    });

    const natija = await response.json();
    document.getElementById("result").innerHTML = `<h2>${natija.natija} (${natija.togri} ta to‘g‘ri javob)</h2>`;
});
