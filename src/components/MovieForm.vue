<template>
  <div>
    <h1>Upload Form</h1>
    <form @submit.prevent="saveMovie" id="movieForm" enctype="multipart/form-data">
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
        <input name="title" v-model="formData.title" type="text" class="form-control" required>
      </div>
      <div class="form-group">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" v-model="formData.description" class="form-control" rows="10" required></textarea>
      </div>
      <div class="form-group">
        <label for="poster" class="form-label">Upload Poster</label>
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

const saveMovie = async () => {
  try {
    const movieForm = document.getElementById("movieForm");
    const form_data = new FormData(movieForm);

    const response = await fetch("/api/v1/movies", {
      method: "POST",
      body: form_data
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    result.value = data;
  } catch (error) {
    console.error('Fetch error:', error);
    result.value = { errors: ["An error occurred while processing your request."] };
  }
};

const handleFileChange = (e) => {
  formData.value.poster = e.target.files[0];
};

onMounted(async () => {
  // Fetch CSRF token
  try {
    const response = await fetch('/api/v1/csrf-token');
    const data = await response.json();
    // Set CSRF token
    document.querySelector('meta[name="csrf-token"]').setAttribute('content', data.csrf_token);
  } catch (error) {
    console.error('Fetch error:', error);
  }
});
</script>

<style>
form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group > label {
  font-weight: bold;
}

input[type="submit"] {
  width: 100px;
  border: none;
  background-color: rgb(76, 120, 240);
  border-radius: 5%;
  color: #fff;
  cursor: pointer;
}

input[type="submit"]:hover {
  background-color: rgb(6, 24, 104);
}

.alert {
  padding-left: 50px;
}
</style>
