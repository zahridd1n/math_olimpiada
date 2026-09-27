<template>
  <section id="yonalishlar" class="editorial-section directions-editorial-section">
    <div class="container">
      <div class="dir-header">
        <div class="header-kicker">
          <span class="editorial-label">Hackathon IT School Dasturlari</span>
          <span class="editorial-tag">[ 03 ]</span>
        </div>
        <h2 class="dir-title">
          Kelajak kasblariga eltuvchi <span class="serif-italic-gold">ta'lim</span> <span class="serif-italic">yo'nalishlari</span>
        </h2>
        <p class="dir-sub">
          Olimpiadada ishtirok etgan iqtidorli o'quvchilar maktabimizda quyidagi yo'nalishlar bo'yicha grant asosida yoki maxsus guruhlarda ta'lim olishlari mumkin.
        </p>
      </div>

      <!-- Linear Editorial Catalog (No generic cards) -->
      <div class="editorial-catalog">
        <div v-for="(dir, i) in directions" :key="i" class="catalog-row">
          <div class="cat-num">0{{ i + 1 }}</div>
          <div class="cat-title-block">
            <h3 class="cat-title">{{ dir.title }}</h3>
            <span class="editorial-tag">[ Amaliy kurs ]</span>
          </div>
          <div class="cat-desc-block">
            <p class="cat-desc">{{ dir.description }}</p>
          </div>
          <div class="cat-action">
            <router-link to="/register" class="cat-arrow-link" aria-label="Batafsil">
              <span>Batafsil</span>
              <span class="arrow">→</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { siteConfig } from '../config/site.js'
const directions = siteConfig.directions
</script>

<style scoped>
.directions-editorial-section {
  background-color: var(--bg-section-4);
  position: relative;
}

.dir-header {
  max-width: 760px;
  margin-bottom: 56px;
}

.header-kicker {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 18px;
}

.dir-title {
  font-size: clamp(2.2rem, 3.8vw, 3.2rem);
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 18px;
}

.dir-sub {
  font-size: 1.05rem;
  line-height: 1.7;
  color: var(--text-secondary);
}

/* Linear Catalog */
.editorial-catalog {
  display: flex;
  flex-direction: column;
  border-top: 1px solid var(--border-subtle);
}

.catalog-row {
  display: grid;
  grid-template-columns: 80px 1.2fr 1.8fr auto;
  align-items: center;
  gap: 32px;
  padding: 32px 0;
  border-bottom: 1px solid var(--border-subtle);
  transition: all 0.25s ease;
}

.catalog-row:hover {
  background: rgba(255, 255, 255, 0.015);
  padding-left: 16px;
  padding-right: 16px;
}

.cat-num {
  font-family: var(--font-mono);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--gold);
}

.cat-title-block {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.cat-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.3;
}

.cat-desc {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-secondary);
  margin: 0;
}

.cat-action {
  display: flex;
  justify-content: flex-end;
}

.cat-arrow-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--text-secondary);
  transition: all 0.2s ease;
}

.cat-arrow-link .arrow {
  transition: transform 0.2s ease;
}

.catalog-row:hover .cat-arrow-link {
  color: var(--gold);
}

.catalog-row:hover .cat-arrow-link .arrow {
  transform: translateX(4px);
}

@media (max-width: 992px) {
  .catalog-row {
    grid-template-columns: 60px 1fr;
    gap: 16px;
  }
  .cat-desc-block {
    grid-column: 2 / 3;
  }
  .cat-action {
    grid-column: 2 / 3;
    justify-content: flex-start;
  }
}
</style>
