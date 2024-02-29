package com.ssafy.adrec.jwt.service;

import com.ssafy.adrec.jwt.Token;
import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jws;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.context.request.RequestContextHolder;
import org.springframework.web.context.request.ServletRequestAttributes;

import javax.servlet.http.HttpServletRequest;
import java.io.UnsupportedEncodingException;
import java.security.Key;
import java.util.Date;
import java.util.Map;

@Service
@Slf4j
public class JwtServiceImpl implements JwtService {

    private final String salt;
    private final String secret;
    private Key key;

    private static final int ACCESS_TOKEN_EXPIRE_MINUTES = 30;

    public JwtServiceImpl(@Value("${jwt.secret}") String secret, @Value("${jwt.salt}") String salt) {
        this.secret = secret;
        this.salt = salt;
        afterPropertiesSet();
    }

    // 주입받은 secret 값을 Base64 Decode 해서 key 변수에 할당
    @Override
    public void afterPropertiesSet() {
        byte[] keyBytes = Decoders.BASE64.decode(secret);
        this.key = Keys.hmacShaKeyFor(keyBytes);
    }

    //Token 발급
    /**
     * key : Claim의 key 값
     * data : Claim의 data 값
     * subject : payload에 sub의 value로 들어갈 subject값
     * expire : 토큰 유효기간
     */

    @Override
    public Token create(String subject) {
        String authority = "USER";

        long now = (new Date()).getTime();

        //Access Token 생성
        String accessToken = Jwts.builder()
                .setSubject(subject)
                .claim("auth", authority)
                .setExpiration(new Date(now + 1000 * 60 * ACCESS_TOKEN_EXPIRE_MINUTES))
                .signWith(key, SignatureAlgorithm.HS256)
                .compact();

        return Token.builder()
                .access(accessToken)
                .build();
    }

    // Signature 설정에 들어갈 key 생성.
    private byte[] generateKey() {
        byte[] key = null;
        try {
            key = salt.getBytes("UTF-8");
        } catch (UnsupportedEncodingException e) {
            if (log.isInfoEnabled()) {
                e.printStackTrace();
            } else {
                log.error("Making JWT Key Error ::: {}", e.getMessage());
            }
        }

        return key;
    }

    // 전달 받은 토큰이 제대로 생성된 것인지 확인
    @Override
    public boolean checkToken(String jwt) {
        try {
            Jws<Claims> claims = Jwts.parser().setSigningKey(this.generateKey()).parseClaimsJws(jwt);
            log.debug("claims: {}", claims);
            return true;
        } catch (Exception e) {
            log.error(e.getMessage());
            return false;
        }
    }

    // access token 가져옴
    @Override
    public Map<String, Object> get(String key) {
        HttpServletRequest request = ((ServletRequestAttributes) RequestContextHolder.currentRequestAttributes())
                .getRequest();
        String jwt = request.getHeader("access-token");
        Jws<Claims> claims = null;
        try {
            claims = Jwts.parser().setSigningKey(salt.getBytes("UTF-8")).parseClaimsJws(jwt);
        } catch (Exception e) {
            log.error(e.getMessage());
        }
        Map<String, Object> value = claims.getBody();
        log.info("value : {}", value);
        return value;
    }

}
