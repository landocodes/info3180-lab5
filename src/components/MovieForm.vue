<!-- MovieForm.vue -->
<template>
  <form id="movieForm" @submit.prevent="saveMovie">
    <div class="form-group mb-3">
      <label for="title" class="form-label">Movie Title</label>
      <input
        v-model="formData.title"
        type="text"
        name="title"
        class="form-control"
      />
    </div>
    <div class="form-group mb-3">
      <label for="description" class="form-label">Description</label>
      <textarea
        v-model="formData.description"
        name="description"
        class="form-control"
      ></textarea>
    </div>
    <div class="form-group mb-3">
      <label for="poster" class="form-label">Poster</label>
      <input
        type="file"
        ref="poster"
        @change="handlePosterChange"
        class="form-control-file"
      />
    </div>
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
</template>

<script setup>
import { ref, onMounted } from "vue";
onMounted(() => {
getCsrfToken();
});

let csrf_token = ref("");

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    });
}

const formData = ref({
  title: '',
  description: '',
  poster: null,
});

const handlePosterChange = () => {
  formData.poster = $refs.poster.files[0];
};

function saveMovie() {
    let movieForm = document.getElementById('movieForm');
    let form_data = new FormData(movieForm);

    fetch("/api/v1/movies", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value
        }
    })
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        // display a success message
        console.log(data);
    })
    .catch(function (error) {
        console.log(error);
    });
}
</script>
