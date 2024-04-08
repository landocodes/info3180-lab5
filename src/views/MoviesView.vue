<template>
  <div>
    <h1>All Movies</h1>
    <div v-if="movies.length === 0">Loading...</div>
    <div v-else>
      <div v-for="movie in movies" :key="movie.id" class="card">
        <img :src="movie.poster" alt="Movie Poster" class="card-img-top">
        <div class="card-body">
          <h5 class="card-title">{{ movie.title }}</h5>
          <p class="card-text">{{ movie.description }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let movies = ref([]);

const fetchMovies = async () => {
  try {
    const response = await fetch('/api/v1/movies');
    const data = await response.json();
    movies.value = data.movies;
  } catch (error) {
    console.error('Fetch error:', error);
  }
};

onMounted(fetchMovies);
</script>

<style scoped>
.card {
  margin-bottom: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
}

.card-img-top {
  width: 100%;
  height: auto;
}
</style>
