<script setup>
import { Icon } from '@iconify/vue';

defineProps({
  workspace: {
    type: Object,
    required: true,
    validator: (obj) => 'id' in obj && 'name' in obj,
  },
});
</script>
<template>
  <div class="w-60 bg-gradient-to-b from-amber-400 to-amber-300 border-r-amber-800 border-r-2 h-screen shadow-lg">
    <div class="p-4 w-full aspect-square text-center">
      <h3 class="text-lg font-bold text-amber-900">{{ workspace.name }}</h3>
      <p class="text-sm text-amber-800">ID: {{ workspace.id }}</p>
    </div>
    <ul class="list-none mx-4">
      <li class="border-b border-amber-700">
        <a :href='`/workspaces/${workspace.id}`' class="py-4 flex items-center gap-x-2 text-amber-900 hover:text-amber-700 transition-colors">
          <Icon icon="material-symbols:home" />
          Home
        </a>
      </li>
      <li class="border-b border-amber-700">
        <a :href='`/workspaces/${workspace.id}/meetups`' class="py-4 flex items-center gap-x-2 text-amber-900 hover:text-amber-700 transition-colors">
          <Icon icon="material-symbols:group" />
          Meetups
        </a>
      </li>
      <li class="border-b border-amber-700">
        <a :href='`/workspaces/${workspace.id}/members`' class="flex py-4 items-center gap-x-2 text-amber-900 hover:text-amber-700 transition-colors">
          <Icon icon="material-symbols:group" />
          Members
        </a>
      </li>
      <li>
        <a :href='`/workspaces/${workspace.id}/settings`' class="flex py-4 items-center gap-x-2 text-amber-900 hover:text-amber-700 transition-colors">
          <Icon icon="material-symbols:settings" />
          Settings
        </a>
      </li>
    </ul>
  </div>
</template>
