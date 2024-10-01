<script setup lang="ts">
import { ref } from 'vue'
import axios from 'axios'

const data = ref(null)
const errorMsg = ref('')

const apiBaseURL = import.meta.env.VITE_API_BASE_URL
if (!apiBaseURL) {
  throw new Error('VITE_API_BASE_URL is not defined')
}

const apiClient = axios.create({
  baseURL: apiBaseURL
})

async function fetchData() {
  errorMsg.value = ''
  try {
    const res = await apiClient.get('/items/')
    data.value = res.data
  } catch (error) {
    data.value = null
    if (axios.isAxiosError(error)) {
      console.error(error)
      errorMsg.value = error.message
    } else {
      console.error(error)
    }
  }
}
</script>

<template>
  <div v-if="errorMsg" role="alert" class="alert alert-error">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="h-6 w-6 shrink-0 stroke-current"
      fill="none"
      viewBox="0 0 24 24"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
      />
    </svg>
    <span>{{ errorMsg }}</span>
  </div>
  <div v-else class="rounded-box bg-base-200 mt-4 p-4">
    <p class="font-bold mb-2">API data:</p>
    <pre v-if="data">{{ data }}</pre>
    <p v-else>No data</p>
  </div>
  <button @click="fetchData" class="btn btn-primary mt-4">Fetch data</button>
</template>
