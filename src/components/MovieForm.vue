<template>
  <div>
    <h1>Upload Form</h1>
    <form @submit.prevent="saveMovie" id="movieForm">
      <div v-if="result.errors">
        <ul class="alert alert-danger">
          <li v-for="error in result.errors" :key="error">{{ error }}</li>
        </ul>
      </div>
      <div v-if="result.message">
        <div class="alert alert-success">{{ result.message }}</div>
      </div>
      <div class="form-group">
        <label for="title" class="form-label">Movie Title</label>
        <input name="title" type="text" class="form-control" v-model="formData.title" required>
      </div>
      <div class="form-group">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control" rows="10" v-model="formData.description" required></textarea>
      </div>
      <div class="form-group">
        <label for="poster" class="form-label">Upload file</label>
        <input type="file" name="poster" class="form-control-file" @change="handleFileChange" required>
      </div>
      <input type="submit" class="btn btn-primary" value="Submit">
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const formData = ref({
  title: '',
  description: '',
  poster: null
});
const result = ref({});
const csrf_token = ref("");

const getCsrfToken = () => {
  fetch('/api/v1/csrf-token')
    .then(res => res.json())
    .then(data => {
      csrf_token.value = data.csrf_token;
    })
    .catch(err => console.error(err));
};

onMounted(() => {
  getCsrfToken();
});

const saveMovie = () => {
  const movieForm = document.getElementById("movieForm");
  const form_data = new FormData(movieForm);

  fetch("/api/v1/movies", {
    method: "POST",
    body: form_data,
    headers: {
      'X-CSRFToken': csrf_token.value
    }
  })
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    result.value = data;
  })
  .catch(error => {
    console.error('Fetch error:', error);
    result.value = { errors: ["An error occurred while processing your request."] };
  });
};

const handleFileChange = (e) => {
  formData.value.poster = e.target.files[0];
};
</script>

<style>
/* Your styles here */
</style>
