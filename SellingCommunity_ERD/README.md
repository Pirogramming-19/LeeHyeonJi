ERD CLOUD 링크: https://www.erdcloud.com/d/vGF5JvtPqFMseiTAz
### 설계한 ERD: ![ERD_IMG](erd.png)
<br>

### challenge 구현한 방법
* 주소(Address) 엔티티 추가
* 대댓글 기능 구현을 위해 커뮤니티댓글 엔티티, 판매댓글 엔티티에 각각 댓글번호, 댓글깊이 컬럼 추가
* 해시태그 기능 구현을 위해 해시태그 엔티티 추가<br>
유저태그 기능 구현을 위해 유저태그 엔티티 추가
* 유저 간의 팔로워, 팔로잉 기능 구현을 위해 팔로우(Follow) 엔티티 추가