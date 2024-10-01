<script setup lang="ts">
import { RouterLink } from 'vue-router'
import NavMenu from './NavMenu.vue'
</script>

<template>
  <div class="navbar bg-base-100">
    <div class="navbar-start">
      <div class="dropdown">
        <div tabindex="0" role="button" class="btn btn-ghost lg:hidden">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-5 w-5"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h8m-8 6h16"
            />
          </svg>
        </div>
        <NavMenu
          tabindex="0"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
        />
      </div>
      <RouterLink to="/" class="btn btn-ghost text-xl">
        <img alt="Vue logo" class="mr-2" src="@/assets/logo.svg" width="32" height="32" />
        My web app</RouterLink
      >
    </div>
    <div class="navbar-center hidden lg:flex"></div>
    <div class="navbar-end">
      <NavMenu class="menu menu-horizontal px-1" />
    </div>
  </div>
</template>
