const form = document.getElementById("edit-form")

form.addEventListener('submit', async (event) => {
  event.preventDefault()

  const url = window.location.href.split("/")
  const id = Number(url[url.length - 1])
  const titulo = document.getElementById("titulo").value
  const detalhes = document.getElementById("detalhes").value
  
  await fetch(`/update/id=${id}&titulo=${titulo}&detalhes=${detalhes}`, {
    method: "POST"
  })

  window.location.replace("/")
})
